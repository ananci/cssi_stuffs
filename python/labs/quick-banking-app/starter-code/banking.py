#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):

    def __init__(self, label, balance):
        self.label = label
        self.balance = balance

    def __str__(self):
        return 'Account Name: {name}\nCurrent Balance: {balance}'.format(
            name=self.label, balance=self.balance)

    def withdraw(self, how_much):
        if how_much <= self.balance and how_much > 0:
            self.balance = self.balance - how_much

    def deposit(self, how_much):
        if how_much > 0:
            self.balance = self.balance + how_much

    def rename(self, name):
        if name != '':
            self.label = name

    def transfer(self, dest_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            dest_account.balance = dest_account.balance + amount
