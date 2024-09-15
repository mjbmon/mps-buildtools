#!/bin/sh

# Usage:
#    build-tarball PROJECT_TOP_DIR TARBALL_NAME
#
#  TARBALL_NAME does NOT include .tar.gz
#

PROJECT_TOP_DIR=$1
if [ "$PROJECT_TOP_DIR" = "" ] ; then echo "PROJECT_TOP_DIR not specified" ; exit 1; fi

TARBALL_NAME=$2
if [ "$TARBALL_NAME" = "" ] ; then echo "TARBALL_NAME not specified" ; exit 1; fi

echo " PROJECT_TOP_DIR ${PROJECT_TOP_DIR}"
echo " TARBALL_NAME    ${TARBALL_NAME}"
echo " MPS_BUILDTOOLS  ${MPS_BUILDTOOLS}"

if [ ! -d "${PROJECT_TOP_DIR}" ] ; then echo "PROJECT_TOP_DIR ${PROJECT_TOP_DIR} is not a directory." ; exit 1; fi

mytmpdir=$(mktemp -d 2>/dev/null || mktemp -d -t 'mytmpdir')

echo " TEMP build directory ${mytmpdir}"
if [ "$mytmpdir" = "" ] ; then echo "mytmpdir failed" ; exit 1; fi
if [ ! -d "$mytmpdir" ] ; then echo "mytmpdir was not created" ; exit 1; fi

mkdir ${mytmpdir}/${TARBALL_NAME}
echo "TEMP SOURCE ${mytmpdir}/${TARBALL_NAME}"

echo "cp -r ${PROJECT_TOP_DIR}/* ${mytmpdir}/${TARBALL_NAME}"
cp -r ${PROJECT_TOP_DIR}/* "${mytmpdir}/${TARBALL_NAME}"
if [ "${MPS_BUILDTOOLS}" != "" ]
then
  cp -r "${MPS_BUILDTOOLS}" "${mytmpdir}/${TARBALL_NAME}"
fi

j=`pwd`
cd ${mytmpdir}
echo "tar cf ${TARBALL_NAME}.tar ${TARBALL_NAME}"
tar cf ${TARBALL_NAME}.tar ${TARBALL_NAME}
gzip ${TARBALL_NAME}.tar
cd $j

cp ${mytmpdir}/${TARBALL_NAME}.tar.gz .

rm -rf ${mytmpdir}
ls -al ${TARBALL_NAME}.tar.gz
