import requests as rq
import warnings
import numpy as np


class Mapper(object):

    """
    The uniprotmapper.Mapper object is used to perform mapping queries over the web using the uniprot programmatic
    interface.

    """

    def __init__(self, url="http://uniprot.org/mapping/",package_params=None):
        self.base_url = url
        self.params = package_params


    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, url):
        if not isinstance(url, str):
            raise TypeError("base url must be a string")
        elif "http" not in url:
            raise ValueError("url should start with 'http' or 'https'")
        elif "uniprot" not in url:
            warnings.warn("'uniprot' was not detected in the url you included. I can make no guarantee that any requests will behave as expected.")
        else:
            self._base_url = url

    @property
    def params(self):
        return self._package

    @params.setter
    def params(self, package_params):
        if package_params is None:
            self._package = {}
        elif not isinstance(package_params, dict):
            raise TypeError("Params must be a dictionary!")
        else:
            self._package = package_params


    def _check_params(self):
        """
        An internal method to check if required parameters exist to perform a database request.
        :return: None. It may raise an Error if the required parameters are not found
        """
        error_message = "'{p}' parameter was not found. Please include that parameter before attempting to ping the uniprot server"
        if "from" not in self.params:
            raise ValueError(error_message.format(p="from"))
        elif "to" not in self.params:
            raise ValueError(error_message.format(p="to"))
        elif "format" not in self.params:
            raise ValueError(error_message.format(p="format"))
        elif "query" not in self.params:
            raise ValueError(error_message.format(p="query"))

        return

    def _format_query(self):
        """
        An internal method to make sure that the 'query parameter is properly formatted'

        :return: None, mutates the self.params['query']  object.
        """
        if isinstance(self.params["query"], list):
            self.params["query"] = " ".join(self.params["query"])
        elif isinstance(self.params["query"], np.ndarray):
            self.params["query"] = " ".join(self.params["query"].tolist())
        elif not isinstance(self.params["query"], basestring):
            raise TypeError("uniprotmapper.Mapper.params['query'] must be either a string, list, or numpy array!")

    def get_data(self, **kwargs):
        """
        This function gets the data from the base url based on the parameters queried. Each parameter that is part of the
        request should be entered as a keyword argument. The input kwargs will be appended to the existing 'params'. A
        few parameters must always be specified before making a request (consult http://www.uniprot.org/help/programmatic_access
        for further information):

        from: the starting database for the mapping
        to: the database to do the mapping to
        format: the format the data should be returned in
        query: the ids to be queried. they should be input as a list here, and will be properly formatted to be sent up
        to uniprot for the request.

        :param kwargs: keyword arguments which specify the parameters for the request. for example, if human data is
        required set 'organism=9606'. As many or as few keyword arguments may be used. A minimum number of kwargs is
        required for a request, as described above.
        :return: a requests.response object with the response from the uniprot server
        """

        self.params.update(kwargs)
        self._check_params()
        self._format_query()

        #ok, seems like we are good to go
        req = rq.get(self.base_url, params=self.params)

        return req
