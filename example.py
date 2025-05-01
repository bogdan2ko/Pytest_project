from db import session
import tables

# value_for_search = 156
# result =session.query(tables.Films).filter(
#     tables.Films.actor_id>value_for_search,
#     tables.Films.actor_id<200).all()

# film_ids = [film.actor_id for film in session.query(tables.Films.actor_id).filter(tables.Films.actor_id > 10).all()]
# result = session.query(tables.Films.first_name).filter(tables.Films.actor_id.in_(film_ids)).all()


result=session.query(tables.Films.actor_id, tables.Films.first_name).order_by(tables.Films.first_name).all()


# for film in result:
#     print(film.actor_id, film.first_name) 


# --------------------------------------------------------------------------------------------------------------
# if result:
#     print(f"Film on number {value_for_search} found:{result.first_name}")
# else:
#     print(f"No film with actor_id {value_for_search}.")
# --------------------------------------------------------------------------------------------------------------


# print(result.first_name)

# print(result)
for film in result:
    print(film.actor_id, film.first_name)

