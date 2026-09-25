from . import (
    model_user,                # 1. Users (+ public_key)
    model_location,            # 2. Locations
    model_permission,          # 3. Permissions
    model_ban,                 # 4. Ban
    model_complaint,           # 5. Complaint
    model_complaints_category, # 6. ComplaintsCategory
    model_genre,               # 7. Genre
    model_board_game,          # 8. BoardGames
    model_game_genre,          # 9. GameGenre
    model_mark_board_game,     # 10. MarkBoardGames
    model_game_table,          # 11. GameTables (выступает как 'groups')
    model_games_played,        # 12. GamesPlayed
    model_message,             # 13. Message (адаптировано под E2EE)
    model_message_status,      # 14. MessageStatus
    model_friend_request,      # 15. FriendRequest
    model_user_favorite_game,  # 16. UserFavoriteGame
    model_user_disliked_game,  # 17. UserDislikedGame
    model_table_game,          # 18. TableGame
    model_table_player,        # 19. TablePlayer (выступает как 'group_members')
    model_game_played_user,    # 20. GamePlayedUser
    model_user_preference,     # 21. UserPreferences
    model_user_preferred_genre,# 22. UserPreferredGenre
    model_key_exchange         # 23. KeyExchange (НОВАЯ)
)