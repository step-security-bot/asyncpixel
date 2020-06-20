class Key:
    def __init__(self, success, key, owner, limit, queriesInPastMin, totalQueries):
        """Base class for watchdog stat"""
        self.success = success
        self.key = key
        self.owner = owner
        self.limit = limit
        self.queriesInPastMin = queriesInPastMin
        self.totalQueries = totalQueries

