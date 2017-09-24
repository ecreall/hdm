hdm
===


Contribute
----------

- Issue Tracker: https://github.com/ecreall/hdm/issues
- Source Code: https://github.com/ecreall/hdm


License
-------

The project is licensed under the AGPLv3+.


Getting Started for development
-------------------------------

To run in development mode::

    sudo apt-get update
    sudo apt-get install python-virtualenv python3 python3-dev libxml2-dev libxslt1-dev \
      libjpeg-dev zlib1g-dev libfreetype6-dev libtiff5-dev libzmq3-dev \
      libyaml-dev git  # this is working on debian jessie and ubuntu xenial
    git clone https://github.com/ecreall/hdm.git
    cd hdm
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    pserve development.ini

The application is on http://127.0.0.1:6543


Process
-------

.. figure:: https://raw.githubusercontent.com/ecreall/hdm/master/hdm%20diagram.png
