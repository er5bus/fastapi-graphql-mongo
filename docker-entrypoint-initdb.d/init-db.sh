#!/usr/bin/env bash
echo "Creating users..."

mongo admin --host localhost --eval "db.createUser(
        {user: '${DATABASE_USER}', pwd: '${DATABASE_PASSWORD}',
        roles: [{role: 'readWrite', db: '${DATABASE_NAME}'}]}
    );
    db.createUser(
        {user: '${DATABASE_ROOT}', pwd: '${DATABASE_ROOT_PASSWORD}',
         roles: [{role: 'userAdminAnyDatabase', db: 'admin'}]}
    );"

echo "Users created."


