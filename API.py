from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select
from datetime import datetime


# Flask server setup
port = 8989
host = "0.0.0.0"

app = Flask(__name__)


# Database configuration
DATABASE_URL = "sqlite:///my_database.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define your table schema
my_table = Table('my_table', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('part_id', String),
                   Column('start_time', DateTime),
                   Column('end_time', DateTime),
                   Column('t_diff', Integer),
                   # Add more columns as needed
                   )

# Reflect the table schema from the database
metadata.create_all(engine)

@app.route('/extract', methods=["GET"])
def get_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    limit = request.args.get('limit', type=int)
    part_id = request.args.get('part_id')

    # Create a database session
    with engine.connect() as connection:
        # Start building the query
        query = select([my_table])

        # Filter by start_date if provided
        if start_date:
            query = query.where(my_table.c.start_time >= start_date)

        # Filter by end_date if provided
        if end_date:
            query = query.where(my_table.c.end_time <= end_date)

        # Filter by part_id if provided
        if part_id:
            query = query.where(my_table.c.part_id == part_id)

        # Limit the number of results if provided
        if limit:
            query = query.limit(limit)

        # Execute the query
        result = connection.execute(query)

        # Fetch the results
        data = [dict(row) for row in result]

    return jsonify(data)


# main
if __name__ == "__main__":
    app.run(host=host, port=port)