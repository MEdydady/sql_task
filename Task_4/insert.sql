
-- вводим название артистов
insert into artists (artist_name)
values ('Sting'),('Madonna'),('MC Hammer'),('Sam Smith'),('Kylie Minogue'),('Nelly Furtado'),('Coldplay'),
('Black Eyed Peas');

-- вводим название  стилей
insert into styles (style_name)
values ('pop rock'),('electroclash'),('hip-hop'),('pop'),('dance-pop'),('electronic'),('alternative'),('r&b');


-- вводим название  альбомов
insert into albums (album_name, year_of_release)
values ('My song', 2019),
('American life', 2003),
('Too Legit to Quit', 1991),
('Love Goes', 2020),
('Golden', 2018),
('The Spirit Indestructible', 2013),
('Everyday Life', 2019),
('Monkey Business', 2005);


-- вводим название  трэков
insert into tracks (track_name, track_duration, album_id )
values ('Brand New Day', 356, 1),
('Desert Rose', 356, 1),
('If You Love Somebody Set Them Free', 435, 1),
('Every Breath You Take', 416, 1),
('Demolition Man', 417, 1),
('Cant Stand Losing You', 249, 1),
('Fields of Gold', 346, 1),
('So Lonely', 408, 1),
('Shape of My Hear', 443, 1),
('Message in a Bottle', 446, 1),
('Fragile', 352, 1),
('Walking on the Moon', 416, 1),
('Englishman in New York', 428, 1),
('If I Ever Lose My Faith in You', 409, 1),
('Roxanne', 257, 1);
('American Life', 458, 2),
('Hollywood', 424, 2),
('Im So Stupid', 409, 2),
('Love Profusion', 338, 2),
('Nobody Knows Me', 439, 2),
('Nothing Fails', 449, 2),
('Intervention', 454, 2),
('X-Static Process', 350, 2),
('Mother and Father', 433, 2),
('Die Another Day', 438, 2),
('Easy Ride', 505, 2);

-- вводим название  сборников
insert into collection  (collection_name , year_of_release)
values ('Best Music', 2018),
('RnB Anthems', 2018),
('Best of Rock', 2020),
('Best of Latin Music', 2013),
('Best of Pop', 2000),
('Winter Hits', 2003),
('Summer Hits', 1998),
('Only Hits', 2009);



-- связывающая таблица стилей и артистов
insert into stylesandartists (style_id, artist_id)
values (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8);

-- связывающая таблица артистов и альбомов
insert into artistsandalbums (artist_id, album_id)
values (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8);

-- добавление артиста  который  находиться в 2х жанрах
insert into stylesandartists(style_id, artist_id)
values (5,2);


-- связывающая таблица трэков и  сборников
insert into tracksandcollection  (track_id, collection_id)
values (12, 6);

