from psycopg import connect

#
#
# # conn = connect("postgresql://admin:password@127.0.0.1:5432/bh")
with connect("postgresql://admin:password@127.0.0.1:5432/bh") as conn:
    with conn.cursor() as cur:
        #         cur.execute(
        #             query="""
        #                 CREATE TABLE IF NOT EXISTS blog.users (
        #                     id BIGSERIAL PRIMARY KEY,
        #                     email VARCHAR (128) NOT NULL UNIQUE CHECK (length(email) >= 5 AND email LIKE '*_@*_._*'),
        #                     password CHAR (60) NOT NULL,
        #                     profile_icon VARCHAR NOT NULL DEFAULT ('https://yandex.by/images/search?img_url=https%3A%2F%2Fspecialplantzundert.nl%2Fwp-content%2Fuploads%2F2020%2F06%2Fnot-found-image-15383864787lu.jpg&lr=157&pos=2&rpt=simage&source=serp&text=IMAGE%20NOT%20FOUND'),
        #                     IS_ACTIVE BOOLEAN NOT NULL DEFAULT (false)
        #                 );
        #             """
        #         )
        #         cur.execute(
        #             query="""
        #                 CREATE TABLE IF not exists blog.posts (
        #                     id bigserial primary key,
        #                     user_id bigint not null,
        #                     title varchar (128) not null ,
        #                     body varchar not null ,
        #                     user_id biginteger not null ,
        #                     foreing key (user_id) references blog.users(id) on delete cascade on update cascade
        #                 );
        #             """
        #         )
        categori_name = 'Sport'
        cur.executemany(
            query=f"insert into blog.categories (name) values (%s);",
            params=[(input(), )]
        )
        conn.commit()
