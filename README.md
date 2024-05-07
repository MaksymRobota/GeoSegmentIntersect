# Geo Segment Intersect

> [Django](https://docs.djangoproject.com/en/5.0/)



![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/intro.webp)
## Features


The test project must include (Implement a web api that would):
- Accept two pairs of doubles, representing a segment
- Search internal database and return a list of rectangles that interset the input segment by any of the edges
- Any ORM or raw SQL of a preference
- Storage format/schema can be of any preference
- Consider performance implications for large number of stored rectangles
- Unit/integration tests is a plus

**In progress**

- [x] Accept two pairs of doubles, representing a segment
- [x] Search internal database and return a list of rectangles that interset the input segment by any of the edges
- [x] Any ORM or raw SQL of a preference
- [x] Storage format/schema can be of any preference
- [ ] Consider performance implications for large number of stored rectangles
- [x] Unit/integration tests is a plus

## 💻 Development

- Clone this repository
- Install dependencies using `pip3 install -r requirements.txt`
- Create conf/local_settings.py with DB config and install Postgres

Ex: 

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'geo_app',
          'USER': 'test_admin',
          'PASSWORD': 'admin1234',
          'HOST': 'localhost',
          'PORT': 5432,
          }
      }
 ####
    Postgres:
    `sudo apt-get install --reinstall libpq-dev`
    `pip3 install psycopg2`

        DB console:
            `sudo -u postgres psql`
            `create user test_admin with password 'admin1234';`
            `create database geo_app owner test_admin;`
    
        python3 manage.py migrate

- Run `python3 manage.py runserver` to start in development mode

###  Draw test segments intersect:
  `python draw.py`

###  Start test:
  `python3 manage.py test`

## Used resources:
    https://en.wikipedia.org/wiki/Intersection_(geometry)#Two_line_segments


## Test cases
![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/myplot.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/myplot2.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/myplot3.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/myplot4.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/myplot5.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/myplot6.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/myplot7.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/myplot8.png)


## Api

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/1.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/2.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/3.png)

![Image alt](https://github.com/MaksymRobota/GeoSegmentIntersect/blob/main/assets/4.png)


## License

Made with ❤️