packages <- c("rvest", "stringr", "tidyr", "dplyr", "languageserver", "jsonlite", "rlang")
suppressMessages(install.packages(setdiff(packages, rownames(installed.packages()))))
suppressMessages(library(rvest))
suppressMessages(library(stringr))
suppressMessages(library(tidyr))
suppressMessages(library(dplyr))
suppressMessages(library(languageserver))
suppressMessages(library(jsonlite))
suppressMessages(library(rlang))

url <- 'http://espn.go.com/nfl/superbowl/history/winners'
espnSite <- read_html(url)
espnTable <- html_nodes(espnSite, ".tablehead") %>%  html_table()
tab <- html_nodes(espnSite, "table")
tab[[1]]
tab <- html_table(tab)[[1]]
tab <- tab[-(1:2),]
names(tab) <- c("Number", "Date", "Location", "Result")
tab$Number <- 1:55
tab$Date <- str_replace(tab$Date, "Jan.", "Jan,")
tab$Date <- str_replace(tab$Date, "Feb.", "Fev,")
tab$Date <- format(as.Date(tab$Date, "%h, %d, %Y"),"%d-%m-%Y")
tab <- separate(tab, Result, c('Winner', 'Looser'), sep = ', ', remove = TRUE)
NumberPattern <- "\\d+$"
tab$WinnerScore <- as.numeric(str_extract(tab$Winner, NumberPattern))
tab$LooserScore <- as.numeric(str_extract(tab$Looser, NumberPattern))
tab$Winner <- unlist(lapply(tab$Winner, function(x) gsub(NumberPattern, "", x)))
tab$Looser <- unlist(lapply(tab$Looser, function(x) gsub(NumberPattern, "", x)))
gameretr = as.data.frame(tab)