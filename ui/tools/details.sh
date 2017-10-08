#!/bin/sh 

FILE_CASE_NO=/tmp/case_no
FILE_NONCE=/tmp/nonce
URL=https://app-test.ohf-lesvos.org/api/v1/person/getBalance

CASE_NO=`cat ${FILE_CASE_NO}`
NONCE=`cat ${FILE_NONCE}`

DIRECTORY_STATUS=/var/lib/tomcat8/webapps/ui/status

#
# Create a temp directory to track current user parameters if nescessary
#
if [ ! -d ${DIRECTORY_STATUS} ]; then
  mkdir ${DIRECTORY_STATUS}
  chmod 0777 ${DIRECTORY_STATUS}
fi

JSON_BALANCE=${DIRECTORY_STATUS}/balance.json
JSON_CASE_NO=${DIRECTORY_STATUS}/case_no.json

#echo ${URL}
#echo ${CASE_NO}
#echo ${NONCE}

cat <<EOF > ${JSON_CASE_NO}
{
	"case_no": "${CASE_NO}"
}
EOF

curl -s -o ${JSON_BALANCE} -X POST "${URL}" -H "Accept: application/json" -H "Content-Type: application/json" -d '{"case_no": "'${CASE_NO}'", "nonce": "'${NONCE}'"}'

chown -R tomcat8 ${DIRECTORY_STATUS}
