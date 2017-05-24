from frontera.core.manager import FrontierManager as FronteraFrontierManager
from frontera.settings import Settings


class FrontierManager(FronteraFrontierManager):

    @classmethod
    def from_settings(cls, settings=None):
        """
        Returns a :class:`FrontierManager <frontera.core.manager.FrontierManager>`  instance initialized with \
        the passed settings argument. If no settings is given,
        :ref:`frontier default settings <frontier-default-settings>` are used.
        """
        manager_settings = Settings.object_from(settings)
        return cls(request_model=manager_settings.REQUEST_MODEL,
                               response_model=manager_settings.RESPONSE_MODEL,
                               backend=manager_settings.BACKEND,
                               logger=manager_settings.LOGGER,
                               event_log_manager=manager_settings.EVENT_LOG_MANAGER,
                               middlewares=manager_settings.MIDDLEWARES,
                               test_mode=manager_settings.TEST_MODE,
                               max_requests=manager_settings.MAX_REQUESTS,
                               max_next_requests=manager_settings.MAX_NEXT_REQUESTS,
                               auto_start=manager_settings.AUTO_START,
                               settings=manager_settings,
                               canonicalsolver=manager_settings.CANONICAL_SOLVER)


    def add_seeds(self, seeds):
        """
        Adds a list of seed requests (seed URLs) as entry point for the crawl.

        :param list seeds: A list of :class:`Request <frontera.core.models.Request>` objects.

        :return: None.
        """
        self._check_startstop()
        # self.event_log_manager.add_seeds(seeds)
        self.logger.manager.debug(self._msg('ADD_SEEDS'))
        self._process_components(method_name='add_seeds',
                                 obj=seeds,
                                 return_classes=(list,))
