#!/usr/bin/env python3
"""
a module for password hasing"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    a function to hash the password and return the hashed one
    """
    return bcrypt.hashpw(b"{password}", bcrypt.gensalt(rounds=12))

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    a function to check if the password provided is correct or not
    """
    return bcrypt.checkpw(b"{password}", hashed_password)
