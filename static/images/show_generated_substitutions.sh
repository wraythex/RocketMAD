#!/bin/sh
find ./generated -type f -size 14476c 2>/dev/null -exec cmp -s ./dummy_pokemon.png "{}" ';' -exec echo "{}" ';'