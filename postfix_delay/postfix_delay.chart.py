# -*- coding: utf-8 -*-
# Description: Postfix delivery delay netdata python.d module
# Author: Daniel Morante (tuaris)
# SPDX-License-Identifier: GPL-3.0-or-later

import re

from bases.FrameworkServices.LogService import LogService

DELAY_REGEX = 'delay=([-+]?[0-9]*\.?[0-9]+),'

ORDER = ['delay']

CHARTS = {
    'delay': {
        'options': [None, 'Average Mail Delay', 'seconds', 'delivery', 'postfix.delay', 'line'],
        'lines': [
            ['seconds', None, 'absolute'],
        ]
    }
}


class Service(LogService):
    def __init__(self, configuration=None, name=None):
        LogService.__init__(self, configuration=configuration, name=name)
        self.order = ORDER
        self.definitions = CHARTS
        self.re = DELAY_REGEX
        self.log_path = self.configuration.get('log_path', '/var/log/maillog')
        self.data = dict()

    def check(self):
        if not LogService.check(self):
            return False

        if not self.re:
            self.error("regex not specified")
            return False

        try:
            self.re = re.compile(self.re)
        except re.error as err:
            self.error("regex compile error: ", err)
            return False

        return True

    def get_data(self):
        """
        :return: dict
        """
        raw = self._get_raw_data()
        lines = 0
        data = {'seconds': 0}

        if not raw:
            return None if raw is None else data

        for line in raw:
            match = self.re.search(line)

            if match:
                lines += 1
                delay = match.group(1)
                data['seconds'] += float(delay)

        if lines > 0:
            data['seconds'] = data['seconds'] / lines

        return data
