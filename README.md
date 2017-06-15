# Udacity ND004 - Catalog Full Stack Nanodegree

This project implements all the requirements of the Catalog project. It was implemented within the VM configured and provided in the course.

The included database (`catalog.db`) includes some seed data. None of the seeded items can be edited/deleted because they wouldn't be owned by the the new user that would be created when you sign in.

To test the edit/delete functionality, you'll have to create new items.

If, at any stage, you want to restore the database to its original state, delete it and execute

```
python seed.py
```

### Google Client Secret

This project DOES NOT include the client secret required for signing in with Google. When testing this project, you will have to use your own client secret. You can download this from the Google Cloud Console.

When running the application, make sure that the path to this client secret JSON file is stored in the `ND004_CATALOG_CLIENT_SECRETS_FILE` environment variable.

To set it inline when running the application, execute:

```
ND004_CATALOG_CLIENT_SECRETS_FILE=/vagrant/catalog/private/client_secret.json python application.py
```

OR

```
export ND004_CATALOG_CLIENT_SECRETS_FILE=/vagrant/catalog/private/client_secret.json
python application.py
```

You can then access the project at http://localhost:8000

### JSON End Points

The home page, category list page and item details page also have JSON end points, which can be created by appending `.json` to the URL

- For the home page, use `http://localhost:8000/index.json`
- For items in a particular category use `http://localhost:8000/catalog/CategoryName.json`
- For a single item, use `http://localhost:8000/catalog/CategoryName/ItemName.json`

