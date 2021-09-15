library(nflfastR)
library(ggimage)
library(ggrepel)
library(tidyverse)

#sample sizes
#field position- your own 40-50 or better


pbp <- load_pbp(2000:2019)

down_by_td <- c("time1", "time2", "prob_of_winning", "num of games")
for (i in seq(0,900,15)){
    losing_data <- pbp %>% 
        filter(score_differential <= -4 &
                   score_differential >= -8 &
                   game_seconds_remaining < i+15 &
                   game_seconds_remaining >= i & yardline_100 <= 60 &
                   yardline_100 >= 50)
    
    
    became_tied <- pbp[pbp$game_id %in% losing_data$game_id, ]%>%
        filter(game_half == 'Overtime')%>%
        select(game_id)
    unique_ties <- unique(became_tied)
    show(unique_ties)
    
    
    count_games <- losing_data %>%
        select(game_id)
    unique_games <- unique(count_games)
    num_of_games<- nrow(unique_games)
    
    home_team_win <- losing_data[losing_data$posteam == losing_data$home_team, ] %>%
        filter(result > 0)%>% 
        select(game_id)
    home_team_win <- unique(home_team_win)
    a <- nrow(home_team_win)
    
    away_team_win <- losing_data[losing_data$posteam == losing_data$away_team, ] %>%
        filter(result < 0)%>% 
        select(game_id)
    away_team_win <- unique(away_team_win)
    b <- nrow(away_team_win)
    
    success_games <- rbind(away_team_win, home_team_win, unique_ties)
    success_games <- unique(success_games)
    num_success <- nrow(success_games)
        
    
    
    num_losing_games <- losing_data %>%
        select(game_id)
    num_losing_games <- unique(num_losing_games)
    c <- nrow(num_losing_games)
    
    
    prop1 <- 100 * (num_success)/c
    prop1
    
    vec <- c(i,i+15,prop1, num_of_games)
    down_by_td <- rbind(down_by_td, vec)
    
}
write.csv(down_by_td,"down_by_td15_sec.csv", row.names = TRUE)


down_by_fg <- c("time1", "time2", "prob_of_winning", "num games")
for (i in seq(0,900,15)){
    losing_data <- pbp %>% 
        filter(score_differential <= -1 &
                   score_differential >= -3 &
                   game_seconds_remaining < i+15 &
                   game_seconds_remaining >= i & yardline_100 <= 60 &
                   yardline_100 >= 50)
    
    became_tied <- pbp[pbp$game_id %in% losing_data$game_id,]%>%
        filter(game_half == 'Overtime')%>%
        select(game_id)
    unique_ties <- unique(became_tied)
    
    count_games <- losing_data %>%
        select(game_id)
    unique_games <- unique(count_games)
    num_of_games<- nrow(unique_games)
    
    home_team_win <- losing_data[losing_data$posteam == losing_data$home_team, ] %>%
        filter(result > 0)%>% 
        select(game_id)
    home_team_win <- unique(home_team_win)
    a <- nrow(home_team_win)
    
    away_team_win <- losing_data[losing_data$posteam == losing_data$away_team, ] %>%
        filter(result < 0)%>% 
        select(game_id)
    away_team_win <- unique(away_team_win)
    b <- nrow(away_team_win)
    
    num_losing_games <- losing_data %>%
        select(game_id)
    num_losing_games <- unique(num_losing_games)
    c <- nrow(num_losing_games)
    
    success_games <- rbind(away_team_win, home_team_win, unique_ties)
    success_games <- unique(success_games)
    num_success <- nrow(success_games)
    
    
    prop1 <- 100 * (num_success)/c
    prop1
    
    vec <- c(i,i+15,prop1, num_of_games)
    down_by_fg <- rbind(down_by_fg, vec)
    
}
write.csv(down_by_fg,"down_by_fg15_sec.csv", row.names = TRUE)
