import handlers
from api.v0 import console_handlers

urls = [
    (r"/register", handlers.RegistrationHandler),
    (r"/create", handlers.CreationHandler),
    (r"/set_location", handlers.SetLocationHandler),
    (r"/get_nearby_users", handlers.GetNearbyUsers),
    # (r"/fb_friends", handlers.FacebookHandler),
    # (r"/football_notifications", FootballEvents),
    # (r"/tennis_notifications", TennisEvents),
    (r"/media", handlers.MediaHandler),
    (r"/media_present", handlers.MediaPresentHandler),
    # (r"/media_multipart", handlers.IOSMediaHandler),
    # (r"/cricket_notifications", CricketEvents),
    (r"/set_user_interests", handlers.UserInterestHandler),
    # (r"/set_ios_token_and_return_user_matches", handlers.IOSSetUserDeviceTokenReturnsUsersMatches),
    (r"/get_contact_jids", handlers.ContactJidsHandler),
    (r"/send_app_invite", handlers.SendAppInvitation),
    (r"/user_register_match", handlers.RegisterUserMatchHandler),
    (r"/user_unregister_match", handlers.UnRegisterUserMatchHandler),
    (r"/set_android_token_and_return_user_matches", handlers.AndroidSetUserDeviceTokenReturnsUsersMatches),
    (r"/remove_android_token", handlers.AndroidRemoveUserDeviceId),
    (r"/set_location_privacy", handlers.LocationPrivacyHandler),
    (r"/notify_event", handlers.PushNotificationHandler),
    (r"/register_matches", handlers.RegisterMatchHandler),
    (r"/set_user_info", handlers.SetUserInfoHandler),
    (r"/get_user_info", handlers.GetUserInfoHandler),
    (r"/set_dp", handlers.SetDpHandler),
    (r"/get_dp", handlers.GetDpHandler),
    (r"/get_referral_code", handlers.GetRefrralCodeHandler),
    (r"/redeem_code", handlers.RedeemCodeHandler),
    (r"/friends_watching", handlers.FriendsWatchingHandler),
    (r"/submit_poll_answer", handlers.PollAnswerHandler),
    (r"/exit_discussion", handlers.ExitDiscussionHandler),

    ## console urls
    (r"/news_login", console_handlers.NewsConsoleLogin),
    (r"/news_add_user", console_handlers.NewsConsoleAddUser),
    (r"/news_upload_s3_object", console_handlers.NewsConsoleUploadS3Object),
    (r"/add_article", console_handlers.NewsConsoleAddCuratedArticle),
    (r"/fetch_articles", console_handlers.NewsConsoleFetchArticles),
    (r"/get_article", console_handlers.NewsConsoleGetArticle),
    (r"/edit_article", console_handlers.NewsConsoleEditArticle),
    (r"/delete_article", console_handlers.NewsConsoleDeleteArticle),
    (r"/publish_article", console_handlers.NewsConsolePublishArticle),
    (r"/get_carousel_articles", console_handlers.NewsConsoleGetCarouselArticles),
    (r"/post_carousel_articles", console_handlers.NewsConsolePostArticlesOnCarousel),
    (r"/get_all_discussions", console_handlers.GetDiscussionsHandler),
    (r"/join_discussion", console_handlers.JoinDiscussionsHandler),
    (r"/peek_discussion", console_handlers.PeekDiscussionsHandler)



    # (r"/admin", admin_api.AdminPage),
    # (r"/get_users", admin_api.AdminSelectUsers),
    # (r"/create_user", admin_api.AdminCreateUser),
    # (r"/update_user", admin_api.AdminUpdateUser),
    # (r"/delete_user", admin_api.AdminDeleteUser),
    # (r"/block_user", admin_api.AdminBlockUser)

]