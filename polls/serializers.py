from rest_framework import serializers

class PremiumUserSerializer(serializers.Serializer):
    premium_users = serializers.CharField()
    email = serializers.EmailField()
    personality = serializers.CharField(allow_null=True)

class UserFullSerializer(serializers.Serializer):
    # will return all fields present in values() for Query 1
    # fields are dynamic (we'll pass dicts), so use SerializerMethod style or generic fields
    # simple generic serializer:
    def to_representation(self, instance):
        return instance
    
class CompanyBriefSerializer(serializers.Serializer):
    CompanyName = serializers.CharField(allow_null=True)
    WebSite = serializers.CharField(allow_null=True)
    Industry = serializers.CharField(allow_null=True)
    Revenue = serializers.CharField(allow_null=True)

class ExecutiveSerializer(serializers.Serializer):
    Executive_Names = serializers.CharField(allow_null=True)
    Executive_LinkedInURL = serializers.CharField(allow_null=True)
    Executive_Job_Title = serializers.CharField(allow_null=True)
    CompanyName = serializers.CharField(allow_null=True)

class DigestStatsSerializer(serializers.Serializer):
    opencount = serializers.IntegerField()
    clickcount = serializers.IntegerField()
    Total_recipients = serializers.IntegerField()