import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import utils 

logger = logging.getLogger('polls')

#  Premium Users
class PremiumUsersView(APIView):
    def get(self, request):
        try:
            users = utils.get_premium_users()
            return Response({"status": "success", "results": users}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching premium users: {e}", exc_info=True)
            return Response({"status": "error", "error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#  Active Premium Users
class ActivePremiumUsersView(APIView):
    def get(self, request):
        try:
            users = utils.get_active_premium_users()
            return Response({"status": "success", "results": users}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching active premium users: {e}", exc_info=True)
            return Response({"status": "error", "error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#  Company Revenue
class CompanyRevenueView(APIView):
    def get(self, request):
        try:
            results = utils.get_company_revenue()
            return Response({"status": "success", "results": results}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching company revenue: {e}", exc_info=True)
            return Response({"status": "error", "error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#  Executives Info
class ExecutivesInfoView(APIView):
    def get(self, request):
        logger.info("Fetching executive information...")
        try:
            executives = utils.get_executives_info()
            logger.info(f"Returned {len(executives)} executives.")
            return Response(
                {"status": "success", "results": executives},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error(f"Error fetching executives info: {e}", exc_info=True)
            return Response(
                {"status": "error", "error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

#  Digest Email Stats
class DigestEmailStatsView(APIView):
    def get(self, request):
        digest_id = request.GET.get('digest_id', 28361)
        try:
            results = utils.get_digest_email_stats(digest_id)
            return Response({"status": "success", "results": results}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching digest email stats: {e}", exc_info=True)
            return Response({"status": "error", "error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
