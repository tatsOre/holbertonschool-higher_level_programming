-- List all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.name NOT IN (
      SELECT tv_genres.name FROM tv_genres, tv_show_genres, tv_shows
      WHERE tv_shows.id = tv_show_genres.show_id
      	    AND tv_show_genres.genre_id = tv_genres.id
      	    AND tv_shows.title = 'Dexter')
ORDER BY tv_genres.name;
