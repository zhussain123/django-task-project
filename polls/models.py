# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class LinkedinRequest(models.Model):
    type = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    query = models.CharField(max_length=300, db_collation='utf8mb3_general_ci', blank=True, null=True)
    company_name = models.CharField(max_length=300, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    errordetail = models.TextField(blank=True, null=True)
    responseid = models.ForeignKey('LinkedinResponse', models.DO_NOTHING, db_column='responseid', blank=True, null=True)
    timestamp = models.DateTimeField()
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    queue = models.IntegerField(blank=True, null=True)
    result_count = models.IntegerField(blank=True, null=True)
    return_result_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkedin_request'


class LinkedinResponse(models.Model):
    requestid = models.ForeignKey(LinkedinRequest, models.DO_NOTHING, db_column='requestid', blank=True, null=True)
    name = models.CharField(max_length=200, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    url = models.CharField(max_length=300, db_collation='utf8mb3_general_ci', blank=True, null=True)
    image = models.CharField(max_length=300, db_collation='utf8mb3_general_ci', blank=True, null=True)
    headline = models.CharField(max_length=300, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    personid = models.ForeignKey('Persons', models.DO_NOTHING, db_column='personid', blank=True, null=True)
    parsed = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    companyid = models.ForeignKey('Company', models.DO_NOTHING, db_column='companyid', blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    urn = models.CharField(max_length=100, blank=True, null=True)
    test = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkedin_response'


class LinkedinSearch(models.Model):
    companyname = models.CharField(max_length=300, blank=True, null=True)
    personname = models.CharField(unique=True, max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    found = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkedin_search'


class YahooCurrencies(models.Model):
    abbreviation = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    symbol = models.CharField(max_length=40, db_collation='utf32_bin', blank=True, null=True)
    exchange_rate = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yahoo_currencies'

class User(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    twitterusername = models.CharField(db_column='TwitterUserName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    lastlogindate = models.DateTimeField(db_column='LastLoginDate', blank=True, null=True)  # Field name made lowercase.
    commulativelogin = models.IntegerField(db_column='CommulativeLogin', blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=50, blank=True, null=True)  # Field name made lowercase.
    linkedinusername = models.CharField(db_column='LinkedInUsername', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    linkedinexpiration = models.DateTimeField(db_column='LinkedInExpiration', blank=True, null=True)  # Field name made lowercase.
    linkedinoauthtoken = models.CharField(db_column='LinkedInOauthToken', max_length=300, blank=True, null=True)  # Field name made lowercase.
    linkedinoauthsecret = models.CharField(db_column='LinkedInOauthSecret', max_length=300, blank=True, null=True)  # Field name made lowercase.
    oauthtoken = models.CharField(db_column='OauthToken', max_length=300, blank=True, null=True)  # Field name made lowercase.
    oauthsecret = models.CharField(db_column='OauthSecret', max_length=300, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=250, blank=True, null=True)  # Field name made lowercase.
    twitterintermediate = models.IntegerField(db_column='TwitterIntermediate', blank=True, null=True)  # Field name made lowercase.
    profilepic = models.CharField(db_column='ProfilePic', max_length=300, blank=True, null=True)  # Field name made lowercase.
    linkedinname = models.CharField(db_column='LinkedinName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    receipt = models.CharField(max_length=10, blank=True, null=True)
    receiptdata = models.CharField(db_column='receiptData', max_length=12000, blank=True, null=True)  # Field name made lowercase.
    subscriptionexpiration = models.DateTimeField(db_column='SubscriptionExpiration', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    linkedinlogintime = models.DateTimeField(db_column='LinkedinLoginTime')  # Field name made lowercase.
    activestatus = models.IntegerField(db_column='ActiveStatus', blank=True, null=True)  # Field name made lowercase.
    emailsubscription = models.CharField(db_column='emailSubscription', max_length=20, blank=True, null=True)  # Field name made lowercase.
    linkedinprofilepic = models.CharField(db_column='LinkedinProfilePic', max_length=300, blank=True, null=True)  # Field name made lowercase.
    twitterprofilepic = models.CharField(db_column='TwitterProfilePic', max_length=300, blank=True, null=True)  # Field name made lowercase.
    notifyemail = models.CharField(max_length=250, blank=True, null=True)
    auditentry = models.DateTimeField(blank=True, null=True)
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotioncode = models.CharField(db_column='PromotionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    app_name = models.CharField(max_length=50, blank=True, null=True)
    device_token = models.CharField(max_length=100, blank=True, null=True)
    web_device_token = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    daily_alert_email_subscription = models.CharField(max_length=20)
    test_user = models.IntegerField()
    salesforcelogin = models.CharField(max_length=300, blank=True, null=True)
    salesforcetoken = models.CharField(max_length=300, blank=True, null=True)
    salesforceurl = models.CharField(max_length=300, blank=True, null=True)
    salesforcerefresh = models.CharField(max_length=300, blank=True, null=True)
    isdeleted = models.IntegerField(blank=True, null=True)
    ext = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    personpdfcount = models.CharField(max_length=20, blank=True, null=True)
    companypdfcount = models.CharField(max_length=20, blank=True, null=True)
    user_company_name = models.CharField(max_length=250, blank=True, null=True)
    enterprise_status = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=15, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    person = models.ForeignKey('Persons', models.DO_NOTHING, blank=True, null=True)
    wb_username = models.CharField(max_length=100, blank=True, null=True)
    delegate_permission = models.IntegerField(blank=True, null=True)
    show_daily_iq = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    reporting_user = models.IntegerField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    wb_password = models.CharField(max_length=250, blank=True, null=True)
    is_password_match = models.IntegerField(blank=True, null=True)
    is_wb = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    salesforce_license = models.IntegerField(blank=True, null=True)
    dynamics_license = models.IntegerField(blank=True, null=True)
    xiq_notified = models.CharField(max_length=5, blank=True, null=True)
    signup_appname = models.CharField(max_length=20, blank=True, null=True)
    last_activity = models.DateTimeField(blank=True, null=True)
    profile_quota = models.IntegerField(blank=True, null=True)
    profile_quota_start_date = models.DateTimeField(blank=True, null=True)
    account_quota = models.IntegerField(blank=True, null=True)
    account_quota_start_date = models.DateTimeField(blank=True, null=True)
    industry_quota = models.IntegerField(blank=True, null=True)
    industry_quota_start_date = models.DateTimeField(blank=True, null=True)
    certification_completion_date = models.DateTimeField(blank=True, null=True)
    certification_name = models.CharField(max_length=100, blank=True, null=True)
    certification_tooltip_date = models.DateTimeField(blank=True, null=True)
    gilroy_tooltip_date = models.DateTimeField(blank=True, null=True)
    mappingpopup = models.IntegerField(db_column='mappingPopup', blank=True, null=True)  # Field name made lowercase.
    mapping_tooltip_date = models.DateTimeField(blank=True, null=True)
    user_type = models.CharField(max_length=30, blank=True, null=True)
    ai_certification_completion_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Persons(models.Model):
    contactid = models.AutoField(db_column='ContactId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    twitterhandler = models.CharField(db_column='TwitterHandler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    linkedinhandler = models.CharField(db_column='LinkedInHandler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    biography = models.CharField(max_length=5000, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    linkedinid = models.CharField(db_column='LinkedInId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=20, blank=True, null=True)  # Field name made lowercase.
    followers = models.IntegerField(db_column='Followers', blank=True, null=True)  # Field name made lowercase.
    following = models.IntegerField(db_column='Following', blank=True, null=True)  # Field name made lowercase.
    tweets = models.IntegerField(db_column='Tweets', blank=True, null=True)  # Field name made lowercase.
    twitterid = models.BigIntegerField(db_column='TwitterId', blank=True, null=True)  # Field name made lowercase.
    tweetstatus = models.IntegerField(db_column='TweetStatus', blank=True, null=True)  # Field name made lowercase.
    positiondetails = models.CharField(db_column='PositionDetails', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    reviewflag = models.IntegerField(db_column='ReviewFlag', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=200, blank=True, null=True)  # Field name made lowercase.
    connections = models.CharField(db_column='Connections', max_length=10, blank=True, null=True)  # Field name made lowercase.
    headline = models.CharField(db_column='Headline', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    summary = models.CharField(db_column='Summary', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    speciality = models.CharField(db_column='Speciality', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=200, blank=True, null=True)  # Field name made lowercase.
    imageupload = models.CharField(db_column='Imageupload', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='Imagepath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    personality_archetype = models.ForeignKey('ArchetypeDetails', models.DO_NOTHING, db_column='personality_archetype', blank=True, null=True)
    review_status = models.CharField(max_length=20, blank=True, null=True)
    degree = models.IntegerField(blank=True, null=True)
    personality_type = models.CharField(max_length=20, blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    url_action = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class ArchetypeDetails(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    disc_personality = models.CharField(max_length=2, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archetype_details'
from django.db import models


class Company(models.Model):
    companyid = models.AutoField(db_column='CompanyId', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=250)  # Field name made lowercase.
    twittersearch = models.CharField(db_column='TwitterSearch', max_length=200, blank=True, null=True)  # Field name made lowercase.
    twitterhandler = models.CharField(db_column='TwitterHandler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    logo = models.CharField(max_length=45, blank=True, null=True)
    linkedinhandler = models.CharField(db_column='LinkedInHandler', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ticketsymbol = models.CharField(db_column='TicketSymbol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=300, blank=True, null=True)  # Field name made lowercase.
    stockexchange = models.CharField(db_column='StockExchange', max_length=50, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WebSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reviewflag = models.IntegerField(db_column='ReviewFlag', blank=True, null=True)  # Field name made lowercase.
    companyimage = models.TextField(db_column='CompanyImage', blank=True, null=True)  # Field name made lowercase.
    twitterreviewflag = models.IntegerField(db_column='TwitterReviewFlag', blank=True, null=True)  # Field name made lowercase.
    linkedinreviewflag = models.IntegerField(db_column='LinkedinReviewFlag', blank=True, null=True)  # Field name made lowercase.
    hottopicid = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    auditentry = models.DateTimeField(blank=True, null=True)
    launchpadimage = models.CharField(max_length=1000, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    duns_id = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=25, blank=True, null=True)
    latitude = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    domain = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class CompanyStats(models.Model):
    statid = models.AutoField(db_column='StatId', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='ComanyId', related_name='stats')
    marketcapital = models.CharField(db_column='MarketCapital', max_length=45, blank=True, null=True)  # Field name made lowercase.
    employees = models.CharField(db_column='Employees', max_length=45, blank=True, null=True)  # Field name made lowercase.
    revenue = models.CharField(db_column='Revenue', max_length=45, blank=True, null=True)  # Field name made lowercase.
    quarevenuegrowth = models.CharField(db_column='QuaRevenueGrowth', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ebitda = models.CharField(db_column='Ebitda', max_length=45, blank=True, null=True)  # Field name made lowercase.
    netincome = models.CharField(db_column='NetIncome', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pe = models.CharField(db_column='PE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    shareprice = models.CharField(db_column='SharePrice', max_length=45, blank=True, null=True)  # Field name made lowercase.
    graph = models.CharField(db_column='Graph', max_length=200, blank=True, null=True)  # Field name made lowercase.
    table = models.CharField(db_column='Table', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sharetrend = models.CharField(db_column='ShareTrend', max_length=100, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    number_52weekrange = models.CharField(db_column='52WeekRange', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    eps = models.CharField(db_column='EPS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    peg = models.CharField(db_column='PEG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operatingmargin = models.CharField(db_column='OperatingMargin', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ps = models.CharField(db_column='PS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    annualreport = models.CharField(max_length=500, blank=True, null=True)
    grossprofit = models.CharField(max_length=20, blank=True, null=True)
    week52change = models.CharField(max_length=20, blank=True, null=True)
    current_price = models.CharField(max_length=45, blank=True, null=True)
    currency = models.CharField(max_length=20, db_collation='utf16_general_ci', blank=True, null=True)
    yahoocurrencies = models.ForeignKey('YahooCurrencies', models.DO_NOTHING, db_column='yahoocurrencies', blank=True, null=True)
    fiscalyear = models.CharField(max_length=20, blank=True, null=True)
    stats_revenue = models.CharField(max_length=45, blank=True, null=True)
    company_tickersymbol = models.CharField(max_length=45, blank=True, null=True)
    company_stockexchange = models.CharField(max_length=50, blank=True, null=True)
    active_status = models.IntegerField(blank=True, null=True)
    display_report = models.IntegerField(blank=True, null=True)
    stock_trend_sign = models.CharField(max_length=3, blank=True, null=True)
    stock_trend_value = models.CharField(max_length=25, blank=True, null=True)
    raw_revenue = models.BigIntegerField(blank=True, null=True)
    raw_netincome = models.BigIntegerField(blank=True, null=True)
    raw_marketcapital = models.BigIntegerField(blank=True, null=True)
    raw_grossprofit = models.BigIntegerField(blank=True, null=True)
    raw_employees = models.IntegerField(blank=True, null=True)
    currency_subset = models.CharField(max_length=45, blank=True, null=True)
    sector_yf = models.CharField(max_length=150, blank=True, null=True)
    industry_yf = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_stats'


class LinkedinPerson(models.Model):
    contactid = models.IntegerField(db_column='ContactId', primary_key=True)
    linkedinurl = models.CharField(db_column='LinkedinUrl', max_length=255, blank=True, null=True)
    job_title = models.CharField(db_column='Job_Title', max_length=255, blank=True, null=True)
    requestid = models.ForeignKey('LinkedinRequest', models.DO_NOTHING, db_column='RequestId', blank=True, null=True)  # Field name made lowercase.
    responseid = models.ForeignKey('LinkedinResponse', models.DO_NOTHING, db_column='ResponseId', blank=True, null=True)  # Field name made lowercase.
    searchid = models.ForeignKey('LinkedinSearch', models.DO_NOTHING, db_column='SearchId', blank=True, null=True)  # Field name made lowercase.
    #linkedinurl = models.CharField(max_length=200, blank=True, null=True)
    notify = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    promotion_code = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    email_status = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    #job_title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkedin_person'


class CompanyExecutives(models.Model):
    contactid = models.ForeignKey(
        'LinkedinPerson', models.DO_NOTHING, db_column='ContactId', related_name='executive_links'
    )
    companyid = models.ForeignKey(
        'Company', models.DO_NOTHING, db_column='CompanyId', related_name='executives'
    )
    type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'company_executives'
       


class SavedDigests(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    creation_time = models.DateTimeField()
    digest_id = models.IntegerField(blank=True, null=True)
    emailsent = models.DateTimeField(blank=True, null=True)
    campaign_id = models.CharField(max_length=100, blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)
    text_preview = models.TextField(blank=True, null=True)
    version_uuid = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    contacts_count = models.IntegerField(blank=True, null=True)
    sent_by = models.IntegerField(blank=True, null=True)
    last_sent = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=500, blank=True, null=True)
    send_email_platform = models.IntegerField()
    test_email = models.IntegerField()
    xiq_event = models.IntegerField()
    published_pardot = models.IntegerField(blank=True, null=True)
    wb_user_id = models.IntegerField(blank=True, null=True)
    wb_sent_by = models.IntegerField(blank=True, null=True)
    error_description = models.CharField(max_length=1500, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    user_modified_by = models.ForeignKey('User', models.DO_NOTHING, db_column='user_modified_by', blank=True, null=True)
    pardot_email_id = models.BigIntegerField(blank=True, null=True)
    pardot_list_ids = models.CharField(max_length=150, blank=True, null=True)
    thumbnail = models.CharField(max_length=150, blank=True, null=True)
    workflow_status = models.CharField(max_length=100, blank=True, null=True)
    workflow_ids = models.CharField(max_length=500, blank=True, null=True)
    ai_id = models.CharField(max_length=100, blank=True, null=True)
    initial_prompt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saved_digests'


class MandrillEmailMsg(models.Model):
    mandrill_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    amazon_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    sendgrid_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    creation_date = models.DateTimeField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    recipient_email = models.CharField(max_length=200, blank=True, null=True)
    sender_email = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=150, blank=True, null=True)
    tags = models.CharField(max_length=150, blank=True, null=True)
    smtp_events = models.CharField(max_length=150, blank=True, null=True)
    resends = models.CharField(max_length=150, blank=True, null=True)
    open_count = models.IntegerField(blank=True, null=True)
    click_count = models.IntegerField(blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)
    digestid = models.IntegerField(blank=True, null=True)
    contactid = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    companyname = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    campaign_id = models.CharField(max_length=100, blank=True, null=True)
    is_complain = models.IntegerField(blank=True, null=True)
    email_date = models.DateField(blank=True, null=True)
    unix_time = models.BigIntegerField(blank=True, null=True)
    unix_date = models.BigIntegerField(blank=True, null=True)
    gmail_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mandrill_email_msg'
