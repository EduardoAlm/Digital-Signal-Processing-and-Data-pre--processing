# coding: utf-8
#!/usr/bin/env python
###############################################
from obspy.core import UTCDateTime, read
import glob
import copy
import obspy
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sys
import matplotlib
import os
from datetime import datetime, timedelta
from obspy.core.util import NamedTemporaryFile
from obspy.clients.fdsn import Client as FDSN_Client
from obspy.clients.iris import Client as OldIris_Client
from obspy.core.event import read_events, Catalog
from obspy.geodetics import locations2degrees
from obspy.taup import TauPyModel
from obspy.geodetics.base import gps2dist_azimuth
from matplotlib.dates import date2num
import scipy.io as spio

def get_data (date, latitude, longitude):
    resp_files = '/Users/gsilveira/Documents/MadalenaMatias/dataless/resp/'
    from obspy.clients.fdsn.mass_downloader import RectangularDomain, \
        Restrictions, MassDownloader

    domain = RectangularDomain(minlatitude=-55.5, maxlatitude=latitude,#66.7,
                               minlongitude=-71.5, maxlongitude=longitude)

    restrictions = Restrictions(
        # Get data for a whole year.
        starttime=obspy.UTCDateTime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5]), int(date[6])),
        endtime=obspy.UTCDateTime(2020, 10, 1),
        # Chunk it to have one file per day.
        chunklength_in_sec=3600000,
        # Considering the enormous amount of data associated with continuous
        # requests, you might want to limit the data based on SEED identifiers.
        # If the location code is specified, the location priority list is not
        # used; the same is true for the channel argument and priority list.
        network="GH", station="AKOS", location="*", channel="*",
        # The typical use case for such a data set are noise correlations where
        # gaps are dealt with at a later stage.
        reject_channels_with_gaps=False,
        # Same is true with the minimum length. All data might be useful.
        minimum_length=0.0,
        # Guard against the same station having different names.
        minimum_interstation_distance_in_m=100.0)

    # Restrict the number of providers if you know which serve the desired
    # data. If in doubt just don't specify - then all providers will be
    # queried.
    mdl = MassDownloader(providers=["IRIS"])
    mdl.download(domain, restrictions, mseed_storage = ("../per_hour/{network}/Leslie/{station}/""{channel}.{location}.{starttime}.{endtime}.mseed"), stationxml_storage="stations")