class PuceRouter:
    
    route_app_labels = {
        'sac': 'default',
        'siuce': 'siuce_db',
    }

    def db_for_read(self, model, **hints):
        """Lectura: si el modelo es de 'sac' o 'siuce', lee de su DB."""
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Escritura: si el modelo es de 'sac' o 'siuce', escribe en su DB."""
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # 1. SAC solo vive en 'default'
        if app_label == 'sac':
            return db == 'default'
        
        # 2. SIUCE solo vive en 'siuce_db'
        if app_label == 'siuce':
            return db == 'siuce_db'
            
        # 3. Tablas nativas de Django (admin, auth, sessions, etc.)
        # Solo deben crearse en 'default'
        return db == 'default'