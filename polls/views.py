import logging
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import connection
from rest_framework import status
from django.db.models import Max, F
logger = logging.getLogger('polls')
from .models import (
    User, Company, CompanyStats, LinkedinPerson,
    CompanyExecutives, SavedDigests, MandrillEmailMsg
)

# Premium Users (your DRF version)
class PremiumUsersView(APIView):
    def get(self, request):
        logger.info("Fetching premium users...")
        try:
            users = (
                User.objects.filter(receipt='Unlimited', isdeleted='0')
                .select_related('person', 'person__personality_archetype')
                .values(
                    'email',
                    premium_users=models.F('person__name'),
                    personality=models.F('person__personality_archetype__name'),
                )
            )
            logger.info(f"Returned {len(users)} premium users.")
            return Response(list(users))
        except Exception as e:
            logger.error(f"Error fetching premium users: {e}", exc_info=True)
            return Response({"error": "Internal Server Error"}, status=500)


# Unlimited, Active Users
class ActivePremiumUsersView(APIView):
    def get(self, request):
        logger.info("Fetching active premium users...")
        try:
            users = (
                User.objects.filter(
                    receipt='Unlimited',
                    isdeleted='0',
                    test_user='0',
                    activestatus='1'
                )
                .values()
            )
            logger.info(f"Returned {len(users)} active premium users.")
            return Response(list(users))
        except Exception as e:
            logger.error(f"Error fetching active premium users: {e}", exc_info=True)
            return Response({"error": "Internal Server Error"}, status=500)


# Company Revenue

class CompanyRevenueView(APIView):
    def get(self, request):
        logger.info("Fetching latest company revenue (ORM version)...")
        try:
            # Step 1: get latest timestamp for each company
            latest_timestamps = (
                CompanyStats.objects
                .values('company_id')
                .annotate(latest_timestamp=Max('timestamp'))
            )

            # Step 2: get actual records matching that latest timestamp
            latest_stats = (
                CompanyStats.objects
                .filter(
                    timestamp__in=[
                        item['latest_timestamp']
                        for item in latest_timestamps
                        if item['latest_timestamp']
                    ]
                )
                .select_related('company')
                .values(
    company_ref=F('company__companyid'),
    company_name=F('company__companyname'),
    website=F('company__website'),
    industry=F('company__industry'),
    latest_revenue=F('revenue'),
    last_updated=F('timestamp')
)
                .order_by('-timestamp')
            )

            results = list(latest_stats)
            if not results:
                logger.warning("No company revenue records found.")
                return Response({"message": "No company revenue data found"}, status=404)

            logger.info(f"Returned {len(results)} latest company revenue records.")
            return Response(results)

        except Exception as e:
            logger.error(f"Error fetching company revenue: {e}", exc_info=True)
            return Response({"error": "Internal Server Error"}, status=500)

# Executives Info
class ExecutivesInfoView(APIView):
    def get(self, request):
        logger.info("Fetching executive information...")
        try:
            executives = (
                LinkedinPerson.objects
                .filter(
                    executive_links__companyid__in=[196, 199, 225, 296],
                    executive_links__type='Executive'
                )
                .select_related('executive_links__companyid')
                .values(
    executive_names=models.F('fname'),
    executive_linkedinurl=models.F('linkedinurl'),
    executive_job_title=models.F('job_title'),
    company_display_name=models.F('executive_links__companyid__companyname')
)
            )
            logger.info(f"Returned {len(executives)} executives.")
            return Response(list(executives))
        except Exception as e:
            logger.error(f"Error fetching executives info: {e}", exc_info=True)
            return Response({"error": "Internal Server Error"}, status=500)


# Digest Email Stats

class DigestEmailStatsView(APIView):
    def get(self, request):
        digest_id = request.GET.get('digest_id', 28361)
        logger.info(f"Fetching digest email stats for digest_id={digest_id}...")
        try:
            query = """
                SELECT 
                    SUM(mem.open_count) AS opencount, 
                    SUM(mem.click_count) AS clickcount, 
                    COUNT(DISTINCT mem.recipient_email) AS total_recipients
                FROM saved_digests sd
                JOIN mandrill_email_msg mem 
                    ON sd.campaign_id = mem.campaign_id
                WHERE sd.digest_id = %s
                GROUP BY sd.digest_id
            """
            with connection.cursor() as cursor:
                cursor.execute(query, [digest_id])
                rows = cursor.fetchall()

            results = [
                {
                    "OpenCount": row[0],
                    "ClickCount": row[1],
                    "TotalRecipients": row[2],
                }
                for row in rows
            ]

            if not results:
                logger.warning(f"No data found for digest_id={digest_id}")
                return Response({"message": "No data found"}, status=404)

            logger.info(f"Returned {len(results)} digest stats for digest_id={digest_id}.")
            return Response(results)
        except Exception as e:
            logger.error(f"Error fetching digest email stats: {e}", exc_info=True)
            return Response({"error": "Internal Server Error"}, status=500)
        

