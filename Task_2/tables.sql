CREATE TABLE IF NOT EXISTS  Styles ( 

        style_id SERIAL PRIMARY KEY, 

        style_name VARCHAR(40) UNIQUE NOT NULL 
);
 

CREATE TABLE IF NOT EXISTS  Artists( 

        artist_id SERIAL PRIMARY KEY, 

        artist_name VARCHAR(40) UNIQUE NOT NULL 
); 

 
CREATE TABLE IF NOT EXISTS  StylesandArtists ( 

        style_id INTEGER REFERENCES Styles(style_id), 

        artist_id  INTEGER REFERENCES Artists(artist_id), 

        CONSTRAINT pk_sa PRIMARY KEY (style_id, artist_id) 
); 


CREATE TABLE IF NOT EXISTS  Albums ( 

        album_id SERIAL PRIMARY key,
        
        album_name VARCHAR(40) NOT null, 

        year_of_release INTEGER  NOT NULL 
); 

CREATE TABLE IF NOT EXISTS  ArtistsandAlbums ( 

        artist_id  INTEGER REFERENCES Artists(artist_id), 

        album_id  INTEGER REFERENCES Albums(album_id), 

        CONSTRAINT pk_aa PRIMARY KEY (artist_id, album_id) 
);

CREATE TABLE IF NOT EXISTS  Tracks ( 

        track_id SERIAL PRIMARY KEY, 

        track_name VARCHAR(40) NOT null, 
        
        track_duration INTEGER NOT null,
        
        album_id  INTEGER REFERENCES Albums(album_id)        
);
 

CREATE TABLE IF NOT EXISTS  Collection( 

        collection_id SERIAL PRIMARY KEY, 

        collection_name VARCHAR(40) NOT null, 

        year_of_release INTEGER  NOT null   
); 

 
CREATE TABLE IF NOT EXISTS  Tracksandcollection ( 

        track_id INTEGER REFERENCES Tracks(track_id), 

        collection_id  INTEGER REFERENCES Collection(collection_id), 

        CONSTRAINT pk_tc PRIMARY KEY (track_id, collection_id) 
);

        
       
       