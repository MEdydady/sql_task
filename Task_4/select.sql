-- 1. Количество исполнителей в каждом жанре;
select style_name , count(style_name) from styles s 
join stylesandartists s2  on s.style_id = s2.style_id 
group by style_name;

-- 2. Количество треков, вошедших в альбомы 2019-2020 годов;
select count (a.year_of_release)  from  tracks t
join albums a on t.album_id=a.album_id
where a.year_of_release <= 2020 and a.year_of_release >= 2019;

-- 3. Средняя продолжительность треков по каждому альбому;
select   a.album_name, avg(track_duration)   from tracks t 
join albums a on t.album_id=a.album_id
group by a.album_name;

-- 4. Все исполнители, которые не выпустили альбомы в 2020 году; (Исправленное)
select a.artist_name   from artists a  
where a.artist_name   not in (
	select a.artist_name from artists a
    join artistsandalbums a2  on a.artist_id = a2.artist_id 
    join albums a3  on a3.album_id = a2.album_id
    where a3.year_of_release = 2020
);




-- 5. Названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
select collection_name , artist_name  from collection c 
join tracksandcollection t on c.collection_id = t.collection_id 
join tracks t2 on t.track_id = t2.track_id 
join albums a on t2.album_id = a.album_id 
join artistsandalbums a2 on a.album_id = a2.album_id 
join artists a3 on a2.artist_id = a3.artist_id 
where artist_name like 'Madonna';

-- 6. Название альбомов, в которых присутствуют исполнители более 1 жанра;
select a3.album_name from styles s 
join stylesandartists s2  on s.style_id = s2.style_id 
join artists a on s2.artist_id  = a.artist_id  
join artistsandalbums a2 on a.artist_id = a2.artist_id 
join albums a3 on a2.album_id = a3.album_id
group by a3.album_name
having count(s.style_name) >1;

-- 7. Наименование треков, которые не входят в сборники;
select track_name from tracks t 
left join tracksandcollection t2 on t.track_id = t2.track_id 
left join collection c on t2.collection_id = c.collection_id
group by track_name
having count(c.collection_id)!=1;

-- 8. Исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
select artist_name,t.track_name, t.track_duration  from artists a
join artistsandalbums a2 on a.artist_id = a2.artist_id 
join albums a3 on a2.album_id = a3.album_id 
join tracks t on a3.album_id = t.album_id 
where t.track_duration <= (select min(t.track_duration) from tracks t )

-- 9. Название альбомов, содержащих наименьшее количество треков.(Исправленное)
select a.album_name from albums a 
join tracks t on a.album_id = t.album_id
group by a.album_name 
having count(t.track_id) = (
    select COUNT(track_id) from tracks
	group by album_id
	order by count limit 1
);
