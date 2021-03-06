define({ "api": [
  {
    "type": "post",
    "url": "/specificApis/admin/add",
    "title": "adminAdd",
    "version": "1.0.0",
    "description": "<p>adminAdd</p>",
    "name": "adminAdd",
    "group": "admin",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"create admin success\"\n}",
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
    "filename": "./specificApis/api/admin.py",
    "groupTitle": "admin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/admin/add"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/admin/changePass",
    "title": "changePass",
    "version": "1.0.0",
    "description": "<p>修改密码</p>",
    "name": "changePass",
    "group": "admin",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"change admin's password success\"\n}",
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
    "filename": "./specificApis/api/admin.py",
    "groupTitle": "admin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/admin/changePass"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/admin/checkPass",
    "title": "checkPass",
    "version": "1.0.0",
    "description": "<p>修改密码时检查原密码正确性</p>",
    "name": "checkPass",
    "group": "admin",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"check password success\"\n}",
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
    "filename": "./specificApis/api/admin.py",
    "groupTitle": "admin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/admin/checkPass"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/admin/editConfig",
    "title": "editConfig",
    "version": "1.0.0",
    "description": "<p>修改开始结束时间、要求时长等配置信息</p>",
    "name": "editConfig",
    "group": "admin",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "endTime",
            "description": "<p>endTime</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "startTime",
            "description": "<p>startTime</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "requiredPoints",
            "description": "<p>requiredPoints</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"edit config success\"\n}",
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
    "filename": "./specificApis/api/admin.py",
    "groupTitle": "admin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/admin/editConfig"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/admin/getConfig",
    "title": "getConfig",
    "version": "1.0.0",
    "description": "<p>查看开始结束时间、要求时长等配置信息</p>",
    "name": "getConfig",
    "group": "admin",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"{'startTime':'xxx', ……}\"\n}",
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
    "filename": "./specificApis/api/admin.py",
    "groupTitle": "admin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/admin/getConfig"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/admin/login",
    "title": "login",
    "version": "1.0.0",
    "description": "<p>系统管理员和年级管理员 登录</p>",
    "name": "login",
    "group": "admin",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"grade admin\" or \"admin\"\n}",
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
    "filename": "./specificApis/api/admin.py",
    "groupTitle": "admin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/admin/login"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/admin/logout",
    "title": "logout",
    "version": "1.0.0",
    "description": "<p>系统管理员退出登录</p>",
    "name": "logout",
    "group": "admin",
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
    "filename": "./specificApis/api/admin.py",
    "groupTitle": "admin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/admin/logout"
      }
    ]
  },
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
    "filename": "./specificApis/api/ImportExport.py",
    "groupTitle": "export",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/export"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/uploadStudentInfo",
    "title": "uploadStudentInfo",
    "version": "1.0.0",
    "description": "<p>upload student info &amp; write student infos</p>",
    "name": "uploadStudentInfo",
    "group": "export",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "file",
            "optional": false,
            "field": "file",
            "description": "<p>file</p>"
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
    "filename": "./specificApis/api/ImportExport.py",
    "groupTitle": "export",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/uploadStudentInfo"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/gradeAdmin/GAchangePass",
    "title": "GAchangePass",
    "version": "1.0.0",
    "description": "<p>修改密码</p>",
    "name": "GAchangePass",
    "group": "gradeAdmin",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password_new",
            "description": "<p>password_new</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password_old",
            "description": "<p>password_old</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"change grade_admin's password success\"\n}",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/GAchangePass"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/gradeAdmin/GAcheckPass",
    "title": "GAcheckPass",
    "version": "1.0.0",
    "description": "<p>修改密码时检查原密码正确性</p>",
    "name": "GAcheckPass",
    "group": "gradeAdmin",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"check password success\"\n}",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/GAcheckPass"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/gradeAdmin/GAclassAdd",
    "title": "GAclassAdd",
    "version": "1.0.0",
    "description": "<p>添加班级，并将会创建一个默认班级负责人，此管理员用户名和初始密码与班号相同。</p>",
    "name": "GAclassAdd",
    "group": "gradeAdmin",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"create class and user success\"\n}",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/GAclassAdd"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/gradeAdmin/GAclassDelete",
    "title": "GAclassDelete",
    "version": "1.0.0",
    "description": "<p>删除班级,班级有同学的时候，拒绝删除</p>",
    "name": "GAclassDelete",
    "group": "gradeAdmin",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"delete class success\"\n}",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/GAclassDelete"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/gradeAdmin/GAgetClasses",
    "title": "GAgetClasses",
    "version": "1.0.0",
    "description": "<p>获取当前年级管理员管理的年级下的所有班级</p>",
    "name": "GAgetClasses",
    "group": "gradeAdmin",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"\"\n}",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/GAgetClasses"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/gradeAdmin/gradeAdminAdd",
    "title": "gradeAdminAdd",
    "version": "1.0.0",
    "description": "<p>add grade admin</p>",
    "name": "gradeAdminAdd",
    "group": "gradeAdmin",
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
            "field": "gradeId",
            "description": "<p>gradeId</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"create admin success\"\n}",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/gradeAdminAdd"
      }
    ]
  },
  {
    "type": "post",
    "url": "/specificApis/gradeAdmin/gradeAdminDelete",
    "title": "gradeAdminDelete",
    "version": "1.0.0",
    "description": "<p>delete gradeAdmin</p>",
    "name": "gradeAdminDelete",
    "group": "gradeAdmin",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "username",
            "description": "<p>grade admin username</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"delete admin success\"\n}",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/gradeAdminDelete"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/gradeAdmin/gradeAdminGetAll",
    "title": "gradeAdminGetAll",
    "version": "1.0.0",
    "description": "<p>get All gradeAdmin</p>",
    "name": "gradeAdminGetAll",
    "group": "gradeAdmin",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"{\"username\": admin2018, \"grade\": \"2018\"}\"\n}",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/gradeAdminGetAll"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/gradeAdmin/gradeAdminLogout",
    "title": "gradeAdminLogout",
    "version": "1.0.0",
    "description": "<p>年级管理员退出登录</p>",
    "name": "gradeAdminLogout",
    "group": "gradeAdmin",
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
    "filename": "./specificApis/api/gradeAdmin.py",
    "groupTitle": "gradeAdmin",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/gradeAdmin/gradeAdminLogout"
      }
    ]
  },
  {
    "type": "POST",
    "url": "/specificApis/grade/gradeAdd",
    "title": "gradeAdd",
    "version": "1.0.0",
    "description": "<p>add a grade</p>",
    "name": "gradeAdd",
    "group": "grade",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "grade",
            "description": "<p>grade</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "college",
            "description": "<p>college</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"create grade success\"\n}",
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
    "filename": "./specificApis/api/grade.py",
    "groupTitle": "grade",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/grade/gradeAdd"
      }
    ]
  },
  {
    "type": "POST",
    "url": "/specificApis/grade/gradeDelete",
    "title": "gradeDelete",
    "version": "1.0.0",
    "description": "<p>delete a grade</p>",
    "name": "gradeDelete",
    "group": "grade",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "gradeId",
            "description": "<p>gradeId</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"delete grade success\"\n}",
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
    "filename": "./specificApis/api/grade.py",
    "groupTitle": "grade",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/grade/gradeDelete"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/grade/gradeGetAll",
    "title": "gradeGetAll",
    "version": "1.0.0",
    "description": "<p>get All grade</p>",
    "name": "gradeGetAll",
    "group": "grade",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"{\"grade\": admin2018, \"college\": \"2018\"}\"\n}",
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
    "filename": "./specificApis/api/grade.py",
    "groupTitle": "grade",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/grade/gradeGetAll"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/show/getAllClass",
    "title": "getAllClass",
    "version": "1.0.0",
    "description": "<p>get all class info</p>",
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
    "filename": "./specificApis/api/show.py",
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
    "filename": "./specificApis/api/show.py",
    "groupTitle": "show",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/show/getClassData"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/show/getGradeClass",
    "title": "getGradeClass",
    "version": "1.0.0",
    "description": "<p>get one grades's all class info</p>",
    "name": "getGradeClass",
    "group": "show",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"get class info success\"\n}",
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
    "filename": "./specificApis/api/show.py",
    "groupTitle": "show",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/show/getGradeClass"
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
    "filename": "./specificApis/api/show.py",
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
    "filename": "./specificApis/api/studentData.py",
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
    "filename": "./specificApis/api/studentData.py",
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
    "filename": "./specificApis/api/studentData.py",
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
    "filename": "./specificApis/api/studentData.py",
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
    "filename": "./specificApis/api/studentData.py",
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
    "filename": "./specificApis/api/studentData.py",
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
    "filename": "./specificApis/api/student.py",
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
    "filename": "./specificApis/api/student.py",
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
    "filename": "./specificApis/api/student.py",
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
    "filename": "./specificApis/api/student.py",
    "groupTitle": "student",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/student/get"
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
    "filename": "./specificApis/api/user.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/user/checkPass"
      }
    ]
  },
  {
    "type": "get",
    "url": "/specificApis/user/getUserClassNumber",
    "title": "getUserClassNumber",
    "version": "1.0.0",
    "description": "<p>getUserClassNumber</p>",
    "name": "getUserClassNumber",
    "group": "user",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"error\": 0,\n    \"result\": \"get UserClassNumber success\"\n}",
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
    "filename": "./specificApis/api/user.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/user/getUserClassNumber"
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
    "filename": "./specificApis/api/user.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/user/getUsername"
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
    "filename": "./specificApis/api/user.py",
    "groupTitle": "user",
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
    "group": "user",
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
    "filename": "./specificApis/api/user.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/login/logout"
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
    "filename": "./specificApis/api/user.py",
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
    "filename": "./specificApis/api/user.py",
    "groupTitle": "user",
    "sampleRequest": [
      {
        "url": window.location.origin + "/api/specificApis/user/changePass"
      }
    ]
  }
] });
