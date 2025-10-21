from django.db import models
from django.db import connection, DatabaseError
from django.db.models import F, Value, Max
from django.db.models.functions import Concat
import logging
from polls.models import Company
from .models import User, CompanyExecutives
logger = logging.getLogger('polls')
logger = logging.getLogger(__name__)

#  Premium Users
def get_premium_users():
    try:
        print("Fetching premium users from utils...")

        users = (
            User.objects.filter(receipt='Unlimited', activestatus=1, isdeleted=0, test_user=0)
            .select_related('person__personality_archetype')
            .annotate(
                user_id_alias=F('userid'),
                user_name_alias=F('fullname'),
                personality_type_alias=F('person__personality_type'),
                personality_name_alias=F('person__personality_archetype__name'),
            )
            .values(
                'user_id_alias',
                'user_name_alias',
                'personality_type_alias',
                'personality_name_alias'
            )
        )

        return {
            "status": "success",
            "results": list(users)
        }

    except Exception as e:
        print(f"Error fetching premium users: {e}")
        return {
            "status": "error",
            "message": str(e)
        }
    

# Active Premium Users
def get_active_premium_users():
    try:
        logger.info("Fetching active premium users from utils...")

        # ORM equivalent of your SQL
        users = (
            User.objects.filter(
                receipt='Unlimited',
                activestatus='1',
                emailsubscription='Subscribed',
                test_user='0'
            )
            .values('userid', 'username')
        )

        user_list = list(users)

        if not user_list:
            logger.warning("No active premium users found.")
            return {
                "status": "success",
                "results": []
            }

        return {
            "status": "success",
            "results": user_list
        }

    except Exception as e:
        logger.error(f"Error fetching active premium users: {e}", exc_info=True)
        return {
            "status": "error",
            "results": [],
            "message": str(e)
        }

#  Company Revenue

def get_company_revenue():
    try:
        logger.info("Fetching company revenue (active_status=1) via ORM...")

        companies = (
            Company.objects
            .filter(stats__active_status=1)
            .values(
                company_id_alias=F('companyid'),
                company_name_alias=F('companyname'),
                website_alias=F('website'),
                industry_alias=F('industry'),
                revenue_alias=F('stats__revenue')
            )
            .distinct()
        )

        if not companies:
            logger.warning("No companies found with active revenue stats.")
            return {
                "status": "success",
                "results": [],
                "message": "No active company revenue data found."
            }

        return {
            "status": "success",
            "results": list(companies)
        }

    except DatabaseError as db_err:
        logger.error(f"Database error while fetching company revenue: {db_err}", exc_info=True)
        return {
            "status": "error",
            "message": f"Database error: {db_err}",
            "results": []
        }

    except Exception as e:
        logger.error(f"Unexpected error in get_company_revenue: {e}", exc_info=True)
        return {
            "status": "error",
            "message": str(e),
            "results": []
        }

#  Executives Info

def get_executives_info():
    try:
        logger.info("Fetching executives info from utils...")

        executives = (
            CompanyExecutives.objects
            .filter(
                companyid__in=[196, 199, 225, 296],
                type='Executive'
            )
            .select_related('contactid')
            .annotate(
                name_alias=Concat(
                    F('contactid__fname'),
                    Value(' '),
                    F('contactid__lname')
                ),
                designation_alias=F('contactid__job_title'),
                linkedin_alias=F('contactid__linkedinurl'),
            )
            .values(
                'name_alias',
                'designation_alias',
                'linkedin_alias'
            )
            .order_by('name_alias')
        )

        if not executives:
            logger.warning("No executives found for provided company IDs.")
            return {
                "status": "success",
                "results": [],
                "message": "No executive records found for the given companies."
            }

        return {
            "status": "success",
            "results": list(executives)
        }

    except DatabaseError as db_err:
        logger.error(f"Database error while fetching executives info: {db_err}", exc_info=True)
        return {
            "status": "error",
            "message": f"Database error: {db_err}",
            "results": []
        }

    except Exception as e:
        logger.error(f"Unexpected error in get_executives_info: {e}", exc_info=True)
        return {
            "status": "error",
            "message": str(e),
            "results": []
        }


#  Digest Email Stats
def get_digest_email_stats(digest_id):
    try:
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

        if not rows:
            logger.warning(f"No digest email stats found for digest_id={digest_id}")
            return {
                "status": "success",
                "results": []
            }

        results = [
            {
                "OpenCount": row[0] or 0,
                "ClickCount": row[1] or 0,
                "TotalRecipients": row[2] or 0,
            }
            for row in rows
        ]

        return {
            "status": "success",
            "results": results
        }

    except DatabaseError as db_err:
        logger.error(f"Database error while fetching digest stats for digest_id={digest_id}: {db_err}", exc_info=True)
        return {
            "status": "error",
            "message": f"Database error: {str(db_err)}",
            "results": []
        }

    except Exception as e:
        logger.error(f"Unexpected error in get_digest_email_stats for digest_id={digest_id}: {e}", exc_info=True)
        return {
            "status": "error",
            "message": str(e),
            "results": []
        }
