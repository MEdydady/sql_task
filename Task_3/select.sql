-- название и год выхода альбомов, вышедших в 2018 году;
select album_name, year_of_release  from albums where year_of_release = 2018;

-- название и продолжительность самого длительного трека;
select track_name, track_duration from tracks order by track_duration desc limit 1;

-- название треков, продолжительность которых не менее 3,5 минуты;
select track_name, track_duration from tracks where track_duration >= 350;

-- названия сборников, вышедших в период с 2018 по 2020 год включительно;
select collection_name, year_of_release from collection c  where year_of_release >= 2018 and year_of_release <= 2020;

-- исполнители, чье имя состоит из 1 слова;
select artist_name from artists  where artist_name not like '% %';


-- название треков, которые содержат слово "мой"/"my";
select track_name from tracks where track_name like '%My%';

select track_name from tracks where track_name like '%мой%';