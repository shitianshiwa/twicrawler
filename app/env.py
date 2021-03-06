#!/usr/bin/python3

import logging
import os
import sys
import termcolor


class Env:
    @staticmethod
    def get_environment(env_name: str, default: str = '', required: bool = False) -> str:
        env: str = os.environ.get(env_name, default)
        if required and (default == '') and (env == ''):
            sys.exit(termcolor.colored(f'Error: Please set environment "{env_name}"', 'red'))

        logger.debug(f'Get environment {env_name}={env}')
        return env


logger: logging.Logger = logging.getLogger(__name__)
