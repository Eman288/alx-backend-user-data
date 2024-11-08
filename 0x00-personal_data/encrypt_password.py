#!/usr/bin/env python3
"""
a module for password hasing"""
import bcrypt


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(b"{password}}", bcrypt.gensalt(rounds=12))
