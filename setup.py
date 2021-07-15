import setuptools
from distutils.core import Extension
version = '1.16.0'

setuptools.setup(
    name='e-x',
    version=version,
    scripts=['electrumx_server', 'electrumx_rpc', 'electrumx_compact_history'],
    python_requires='>=3.7',
    install_requires=['aiorpcX[ws]>=0.18.5,<0.19', 'attrs',
                      'plyvel', 'pylru', 'aiohttp>=3.3,<4', 
                      'quark_hash', 'python-dotenv', 'xevan_hash', 
                      'deeponion-x13-hash'],
    extras_require={
        'rapidjson': ['python-rapidjson>=0.4.1,<2.0'],
        'rocksdb': ['python-rocksdb>=0.6.9'],
        'ujson': ['ujson>=2.0.0,<4.0.0'],
        'uvloop': ['uvloop>=0.14'],
        # For various coins
        'blake256': ['blake256>=0.1.1'],
        'crypto': ['pycryptodomex>=3.8.1'],
        'groestl': ['groestlcoin-hash>=1.0.1'],
        'tribushashm': ['tribushashm>=1.0.5'],
        'xevan-hash': ['xevan-hash'],
        'x11-hash': ['x11-hash>=1.4'],
        'zny-yespower-0-5': ['zny-yespower-0-5'],
        'bell-yespower': ['bell-yespower'],
        'cpupower': ['cpupower'],
    },
    packages=setuptools.find_packages(include=('electrumx*',)),
    description='ElectrumX Server',
    author='Electrum developers',
    author_email='electrumdev@gmail.com',
    license='MIT Licence',
    url='https://github.com/spesmilo/electrumx',
    long_description='Server implementation for the Electrum protocol',
    download_url=('https://github.com/spesmilo/electrumX/archive/'
                  f'{version}.tar.gz'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
        'Topic :: Internet',
    ],
    ext_modules=[Extension("x11kvs", 
                               sources = ['x11kvs/algo/groestl/sph_groestl.c',
                                          'x11kvs/algo/blake/sph_blake.c',
                                          'x11kvs/algo/keccak/sph_keccak.c',
                                          'x11kvs/algo/jh/sph_jh.c',
                                          'x11kvs/algo/bmw/sph_bmw.c',
                                          'x11kvs/algo/cubehash/cubehash_sse2.c',
                                          'x11kvs/algo/shavite/sph_shavite.c',
                                          'x11kvs/algo/simd/nist.c',
                                          'x11kvs/algo/simd/vector.c',
                                          'x11kvs/algo/luffa/luffa_for_sse2.c',
                                          'x11kvs/algo/skein/sph_skein.c',
                                          'x11kvs/algo/echo/sph_echo.c',
                                          'x11kvs/algo/sha/sha2.c',
                                          'x11kvs/algo/x11/x11kvs.c',
                                          'x11kvs/x11kvsModule.c'
                                          ],

                               include_dirs=['x11kvs', 'x11kvs/simd-utils', '/usr/include/openssl'
                                            ])]
)
