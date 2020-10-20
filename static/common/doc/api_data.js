define({ "api": [
  {
    "type": "post",
    "url": "/common/keyInfo",
    "title": "apiKey info",
    "version": "1.0.0",
    "description": "<p>Get apiKey info</p>",
    "name": "keyInfo",
    "group": "common",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "key",
            "description": "<p>apiKey</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": {\n        \"name\": \"key name\",\n        \"description\": \"key description\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./common/apis.py",
    "groupTitle": "common",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/common/keyInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "/common/newKey",
    "title": "Create a new apiKey",
    "version": "1.0.0",
    "description": "<p>create a new apiKey</p>",
    "name": "newKey",
    "group": "common",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "name",
            "description": "<p>Key name</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": true,
            "field": "description",
            "description": "<p>Key description</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": {\n        \"value\": \"apiKey here\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./common/apis.py",
    "groupTitle": "common",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/common/newKey"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/export",
    "title": "export",
    "version": "1.0.0",
    "description": "<p>export student info</p>",
    "name": "export",
    "group": "export",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"get all class info success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "export",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/export"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/login/login",
    "title": "login",
    "version": "1.0.0",
    "description": "<p>login</p>",
    "name": "login",
    "group": "login",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "username",
            "description": "<p>username unique</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password",
            "description": "<p>password</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"login\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "login",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/login/login"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/login/logout",
    "title": "logout",
    "version": "1.0.0",
    "description": "<p>logout</p>",
    "name": "logout",
    "group": "login",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"logout\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "login",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/login/logout"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/show/getAllClass",
    "title": "getAllClass",
    "version": "1.0.0",
    "description": "<p>get this grades's all class info</p>",
    "name": "getAllClass",
    "group": "show",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"get all class info success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "show",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/show/getAllClass"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/show/getClassData",
    "title": "getClassData",
    "version": "1.0.0",
    "description": "<p>getClassData</p>",
    "name": "getClassData",
    "group": "show",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "classNumber",
            "description": "<p>classNumber</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"get all class info success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "show",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/show/getClassData"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/show/getStudentData",
    "title": "getStudentData",
    "version": "1.0.0",
    "description": "<p>getStudentData</p>",
    "name": "getStudentData",
    "group": "show",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "studentId",
            "description": "<p>studentId unique</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"get all class info success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "show",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/show/getStudentData"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/studentData/askLeave",
    "title": "askLeave",
    "version": "1.0.0",
    "description": "<p>ask for leave</p>",
    "name": "askLeave",
    "group": "studentData",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "studentId",
            "description": "<p>studentId unique</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"ask for leave success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "studentData",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/studentData/askLeave"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/studentData/getClassStudents",
    "title": "getClassStudents",
    "version": "1.0.0",
    "description": "<p>get this class's students</p>",
    "name": "getClassStudents",
    "group": "studentData",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"ask for leave success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "studentData",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/studentData/getClassStudents"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/studentData/getStudentstates",
    "title": "getStudentStates",
    "version": "1.0.0",
    "description": "<p>getStudentStates</p>",
    "name": "getStudentStates",
    "group": "studentData",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "studentId",
            "description": "<p>studentId unique</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"ask for leave success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "studentData",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/studentData/getStudentstates"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/studentData/signIn",
    "title": "signIn",
    "version": "1.0.0",
    "description": "<p>开始签到</p>",
    "name": "signIn",
    "group": "studentData",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "studentId",
            "description": "<p>studentId unique</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"Record success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "studentData",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/studentData/signIn"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/studentData/signOut",
    "title": "signOut",
    "version": "1.0.0",
    "description": "<p>sign Out</p>",
    "name": "signOut",
    "group": "studentData",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "studentId",
            "description": "<p>studentId unique</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "dataId",
            "description": "<p>dataId unique</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"sign Out success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "studentData",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/studentData/signOut"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/studentData/signOutCron",
    "title": "signOutCron",
    "version": "1.0.0",
    "description": "<p>signOutCron</p>",
    "name": "signOutCron",
    "group": "studentData",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "studentData",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/studentData/signOutCron"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/student/add",
    "title": "studentAdd",
    "version": "1.0.0",
    "description": "<p>studentAdd</p>",
    "name": "studentAdd",
    "group": "student",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "studentId",
            "description": "<p>studentId unique</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "name",
            "description": "<p>name</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "sex",
            "description": "<p>sex</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "state",
            "description": "<p>state</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "initPoints",
            "description": "<p>initial points</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "classNumber",
            "description": "<p>classNumber 外键</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"create student success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "student",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/student/add"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/student/change",
    "title": "studentChange",
    "version": "1.0.0",
    "description": "<p>studentChange</p>",
    "name": "studentChange",
    "group": "student",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "studentId",
            "description": "<p>studentId unique</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "name",
            "description": "<p>name</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "sex",
            "description": "<p>sex</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "classNumber",
            "description": "<p>classNumber 外键</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": change student success\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "student",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/student/change"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/student/delete",
    "title": "studentDelete",
    "version": "1.0.0",
    "description": "<p>Delete student</p>",
    "name": "studentDelete",
    "group": "student",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "studentId",
            "description": "<p>studentId unique</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"delete student success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "student",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/student/delete"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/student/get",
    "title": "studentGet",
    "version": "1.0.0",
    "description": "<p>studentGet</p>",
    "name": "studentGet",
    "group": "student",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": value\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "student",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/student/get"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/test",
    "title": "test",
    "version": "1.0.0",
    "description": "<p>test</p>",
    "name": "test",
    "group": "test",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"create user success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "test",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/test"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/user/checkPass",
    "title": "checkPass",
    "version": "1.0.0",
    "description": "<p>checkPass</p>",
    "name": "checkPass",
    "group": "user",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password",
            "description": "<p>password</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"login\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/user/checkPass"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/user/getUsername",
    "title": "getUsername",
    "version": "1.0.0",
    "description": "<p>get username</p>",
    "name": "getUsername",
    "group": "user",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"get username success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/user/getUsername"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/user/add",
    "title": "userAdd",
    "version": "1.0.0",
    "description": "<p>userAdd</p>",
    "name": "userAdd",
    "group": "user",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "username",
            "description": "<p>username unique</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password",
            "description": "<p>password</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "classNumber",
            "description": "<p>classNumber unique</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "grade",
            "description": "<p>grade</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"create user success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/user/add"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/user/changePass",
    "title": "userChangePass",
    "version": "1.0.0",
    "description": "<p>change user's password</p>",
    "name": "userChangePass",
    "group": "user",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password",
            "description": "<p>new password</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"create user success\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 1,\n    \"reason\": \"error reason here\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./specificApis/apis.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/user/changePass"
      }
    ]
  }
] });
