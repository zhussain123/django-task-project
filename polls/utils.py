from django.db import models
from django.db.models import F, Value
from django.db.models.functions import Concat
import logging
from .models import User, CompanyStats, LinkedinPerson , CompanyExecutives

logger = logging.getLogger('polls')


#  Premium Users
def get_premium_users():
    logger.info("Fetching premium users from utils...")
    users = (
        User.objects.filter(receipt='Unlimited', isdeleted='0')
        .select_related('person', 'person__personality_archetype')
        .values(
            'email',
            premium_users=models.F('person__name'),
            personality=models.F('person__personality_archetype__name'),
        )
    )
    return list(users)


# Active Premium Users
def get_active_premium_users():
    logger.info("Fetching active premium users from utils...")
    users = (
        User.objects.filter(
            receipt='Unlimited',
            isdeleted='0',
            test_user='0',
            activestatus='1'
        )
        .values()
    )
    return list(users)


#  Company Revenue
def get_company_revenue():
    logger.info("Fetching latest company revenue from utils...")
    latest_timestamps = (
        CompanyStats.objects
        .values('company_id')
        .annotate(latest_timestamp=Max('timestamp'))
    )

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
    return list(latest_stats)


#  Executives Info
def get_executives_info():
    logger.info("Fetching executives info (ORM version)...")

    executives = (
        CompanyExecutives.objects
        .filter(
            companyid__in=[196, 199, 225, 296],
            type='Executive'
        )
        .select_related('companyid', 'contactid')
        .annotate(
            CompanyId=F('companyid__companyid'),
            CompanyName=F('companyid__companyname'),
            ExecutiveName=Concat(F('contactid__fname'), Value(' '), F('contactid__lname')),
            JobTitle=F('contactid__job_title'),
            LinkedInURL=F('contactid__linkedinurl'),
        )
        .values('CompanyId', 'CompanyName', 'ExecutiveName', 'JobTitle', 'LinkedInURL')
        .order_by('ExecutiveName')
    )

    return list(executives)

#  Digest Email Stats
def get_digest_email_stats(digest_id):
    logger.info(f"Fetching digest email stats for digest_id={digest_id} from utils...")
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
    return results
