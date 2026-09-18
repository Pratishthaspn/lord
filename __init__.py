with app.app_context():
        from app import models  # noqa: F401  - needed so create_all sees the tables
        try:
            db.create_all()
        except Exception as exc:
            app.logger.warning("create_all skipped: %s", exc)

    return app
