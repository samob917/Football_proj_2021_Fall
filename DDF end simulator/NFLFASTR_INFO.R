library(nflfastR)
library(ggimage)
library(ggrepel)
library(tidyverse)

pbp <- load_pbp(2000:2019)
losing_data <- pbp %>% 
    filter(score_differential < -8 &
               score_differential >= -11 &
               game_seconds_remaining <= 120)
write.csv(losing_data,"real_cases.csv", row.names = TRUE)

home_team_win <- losing_data[losing_data$posteam == losing_data$home_team, ] %>%
    filter(result > 0)%>% 
    select(game_id)
home_team_win <- unique(home_team_win)
nrow(home_team_win)

away_team_win <- losing_data[losing_data$posteam == losing_data$away_team, ] %>%
    filter(result < 0)%>% 
    select(game_id)
away_team_win <- unique(away_team_win)
nrow(away_team_win)
           
           


num_games <- pbp %>%
    select(game_id)
num_games <- unique(num_games)
nrow(num_games)

num_losing_games <- losing_data %>%
    select(game_id)
num_losing_games <- unique(num_losing_games)
nrow(num_losing_games)

losing_data2 <- pbp %>% 
    filter(score_differential < -8 &
               score_differential >= -11 &
               game_seconds_remaining <= 120, game_seconds_remaining >= 60,
           yardline_100 <= 50)
write.csv(losing_data2,"real_cases_overmin.csv", row.names = TRUE)

num_losing2_games <- losing_data2 %>%
    select(game_id)
num_losing2_games <- unique(num_losing2_games)
nrow(num_losing2_games)





became_tied <- pbp[pbp$game_id %in% losing_data$game_id,]%>%
    filter(game_half == 'Overtime')%>%
    select(game_id)

games_to_look_at <- rbind(became_tied, away_team_win, home_team_win)
games_to_look_at <- unique(games_to_look_at)

pbp_interesting_games <- pbp[pbp$game_id %in% games_to_look_at$game_id, ]%>%
    filter(game_seconds_remaining <= 300)
write.csv(pbp_interesting_games,"interesting_games.csv", row.names = TRUE)

potential_comeback <- pbp[pbp$game_id %in% losing_data$game_id, ]%>%
    filter(game_seconds_remaining < 120,
           score_differential >= -8, score_differential<= 0)

comeback_games <- potential_comeback %>%
    select(game_id)
comeback_games <- unique(comeback_games)
nrow(comeback_games)




potential_comeback <- pbp[pbp$game_id %in% losing_data$game_id, ]%>%
    filter(game_seconds_remaining < 120, score_differential < -8,
           score_differential >=-11)%>%
    group_by(play_type)%>%
    summarize(plays = n())%>%
    View()







losing_data %>%
    filter(yardline_100 <= 50)%>%
    View()

losing_data %>%
    filter(yardline_100 < 50 &
               down < 4 & yardline_100 > 20)%>%
    group_by(play_type)%>%
    summarize(plays = n())
losing_data %>%
    filter(yardline_100 < 50 &
               down < 4 & yardline_100 > 20)%>%
    group_by(old_game_id, play_type) %>%
    summarize(plays = n()) %>%
    View()


losing_data %>%
    filter(yardline_100 < 50 &
               down == 4 
           & ydstogo < 2)%>%
    group_by(play_type)%>%
    summarize(plays = n(), description = desc) %>%
    View()








fg_data <- pbp %>% 
    filter(score_differential < -8 &
               score_differential >= -11 &
               game_seconds_remaining <= 120 & 
               play_type == "field_goal") %>%
    select(game_id)

games_with_fg <- pbp[pbp$game_id %in% fg_data$game_id, ]%>%
    filter(game_seconds_remaining <= 300)

fg_data_deliberate <- pbp %>% 
    filter(score_differential < -8 &
               score_differential >= -11 &
               game_seconds_remaining <= 120 & 
               play_type == "field_goal"&
               down < 4) %>%
    select(game_id)

games_with_fgd <- pbp[pbp$game_id %in% fg_data_deliberate$game_id, ]%>%
    filter(game_seconds_remaining <= 300)
write.csv(games_with_fgd,"early_fg.csv", row.names = TRUE)