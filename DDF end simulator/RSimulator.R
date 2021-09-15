#NFL Fast R need drives starting around the 50 

pbp <- load_pbp(2000:2019)

Drive1 <- pbp %>%
  filter(game_seconds_remaining <= 120, score_differential <= -8,
         score_differential >= -16, yardline_100 <= 55,
         yardline_100 >= 45, down == 1, ydstogo == 10) %>%
  select(game_id, drive, drive_end_yard_line,
          desc, game_seconds_remaining, 
        yardline_100, drive_game_clock_end, down, ydstogo, drive_ended_with_score,
        drive_play_id_ended, fixed_drive_result)
write.csv(Drive1,"Drive1.csv", row.names = TRUE)
#392


Drive1b <- pbp %>%
  filter(game_seconds_remaining <= 120, score_differential < 0,
         score_differential >= -16, yardline_100 <= 55,
         yardline_100 >= 45, down == 1, ydstogo == 10) %>%
  select(game_id, drive, drive_end_yard_line,
         desc, game_seconds_remaining, 
         yardline_100, drive_game_clock_end, down, ydstogo, drive_ended_with_score,
         drive_play_id_ended, fixed_drive_result)
write.csv(Drive1b,"Drive1b.csv", row.names = TRUE)
#Now I will save this as a CSV 
#My function is: Drive time remaining = gameseconds remaining - drive game clock end
#Yards = yardline_100 - drive_end_yard_line (when no touchdown)
#num is 312 games
#
#

Drive2_Need_TD <- pbp %>%
  filter(game_seconds_remaining <= 120, score_differential < -3,
         score_differential > -9, yardline_100 <= 65,
         yardline_100 >= 55, down == 1, ydstogo == 10) %>%
  select(game_id, drive, drive_end_yard_line,
         desc, game_seconds_remaining, 
         yardline_100, drive_game_clock_end, down, ydstogo, drive_ended_with_score,
         drive_play_id_ended, fixed_drive_result)
#412
write.csv(Drive2_Need_TD,"Drive2_Need_TD.csv", row.names = TRUE)

Drive2_Need_FG <- pbp %>%
  filter(game_seconds_remaining <= 120, score_differential < 0,
         score_differential > -4, yardline_100 <= 65,
         yardline_100 >= 55, down == 1, ydstogo == 10) %>%
  select(game_id, drive, drive_end_yard_line,
         desc, game_seconds_remaining, 
         yardline_100, drive_game_clock_end, down, ydstogo, drive_ended_with_score,
         drive_play_id_ended, fixed_drive_result)
#316
write.csv(Drive2_Need_FG,"Drive2_Need_FG.csv", row.names = TRUE)


last_play_of_drive <- pbp %>%
  filter(play_id == 3520, game_id == '2000_02_MIA_MIN')%>%
  View()

View(Yard_distribution)

Drive1 <- pbp %>%
  filter(game_seconds_remaining <= 120, score_differential < -3,
         score_differential >= -16, yardline_100 <= 55,
         yardline_100 >= 45, down == 1, ydstogo == 10) %>%
  select(game_id, drive, drive_end_yard_line,
         desc, game_seconds_remaining, 
         yardline_100, drive_game_clock_end, down, ydstogo, drive_ended_with_score,
         drive_play_id_ended, fixed_drive_result)%>%
  View()
