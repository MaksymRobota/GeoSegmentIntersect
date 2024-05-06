# Django

> [Django](https://docs.djangoproject.com/en/5.0/)



![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/intro.webp)
## Features


The test project must include (Implement a web api that would):
- Accept two pairs of doubles, representing a segment
- Search internal database and return a list of rectangles that interset the input segment by any of the edges
- Any ORM or raw SQL of a preference
- Storage format/schema can be of any preference
- Consider performance implications for large number of stored rectangles
- Unit/integration tests is a plus

**In progress**

- [ ] Define API Endpoints /api/search (POST method).
    `{
      "segment": [
        {"x": 10.0, "y": 20.0},
        {"x": 30.0, "y": 40.0}
      ]
    }`
- [ ] Design a database schema to store rectangles efficiently.
  Consider using a spatial database if available (e.g., PostGIS for PostgreSQL).
    `INSERT INTO rectangles (geom) VALUES
      ('POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))'),
      ('POLYGON((5 5, 5 15, 15 15, 15 5, 5 5))');`

  Indexing: Ensure appropriate indexing for efficient querying.
    `SELECT * FROM rectangles
    WHERE geom && 'POLYGON((2 2, 2 8, 8 8, 8 2, 2 2))'::geometry;`
- [ ] Implement the endpoint to accept two pairs of doubles representing a segment.
    *geometric analysis algorithms, such as the Polygonal Intersection algorithm
  Validate input data to ensure it's in the correct format.
  Use appropriate data validation techniques to prevent SQL injection and other security vulnerabilities.
- [ ] Design an algorithm to search for rectangles that intersect with the given segment.
  Utilize spatial indexing or efficient querying techniques to improve performance.
  Consider algorithms like R-tree or Quadtree for spatial indexing.
- [ ] Profile the application to identify performance bottlenecks.
  Implement caching mechanisms to reduce database load.
  Consider asynchronous processing for heavy tasks.
  Implement pagination or limit the number of returned results for large datasets.
  Monitor and tune the database for better performance.
- [ ] Unit/integration tests is a plus.

## 💻 Development

- Clone this repository
- Install dependencies using `pip3 install -r requirements.txt`
- Run `python3 manage.py runserver` to start in development mode

Postgres:
sudo apt-get install --reinstall libpq-dev
pip3 install psycopg2

    DB console:
        sudo -u postgres psql
        create user test_admin with password 'admin1234';
        create database log_app owner test_admin;

    python3 manage.py migrate

Additional commands:
python3 manage.py startapp messenger - Add new module


###  Start test:
  `pytest test_main.py -s`

## License

Made with ❤️