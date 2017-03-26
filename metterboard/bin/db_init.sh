#!/bin/bash
cat metterboard/db_tables/metterboard.sqlite3.sql | sqlite3 metterboard.db
