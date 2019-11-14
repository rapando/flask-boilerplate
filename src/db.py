from sqlalchemy import create_engine


def connect():
    engine = create_engine("mysql+pymysql://sam:therealsam@localhost/testdb")
    connection = engine.connect()
    return connection


# def result_to_dict(results):
#     rows = results.fetchall()
#     keys = results.keys()

#     for row in results:
