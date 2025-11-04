# Manual Testing Guide - LogBERT Monitoring Platform

This guide provides step-by-step instructions for manually testing all features of the LogBERT Remote Monitoring Platform.

---

## Prerequisites

- ✅ Django development server running (`python manage.py runserver`)
- ✅ Virtual environment activated (`source venv/bin/activate`)
- ✅ Database migrations applied (`python manage.py migrate`)
- ✅ Admin user created (`python manage.py createsuperuser`)
- ✅ Sample data loaded (optional: `python manage.py populate_sample_data`)

---

## Test Environment Setup

### 1. Start the Development Server

```bash
cd /home/shun/Desktop/logbert/webplatform
source venv/bin/activate
python manage.py runserver
```

**Expected Output:**
```
Django version 5.2.5, using settings 'webplatform.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### 2. Open Browser

Navigate to: `http://127.0.0.1:8000/`

---

## Manual Test Cases

## 📋 Test 1: Authentication System

### 1.1 Login Page Access
1. **Action**: Navigate to `http://127.0.0.1:8000/auth/login/`
2. **Expected**: Login page displays with username and password fields
3. **Result**: ⬜ Pass / ⬜ Fail

### 1.2 Invalid Login
1. **Action**: Enter invalid credentials (e.g., username: `wrong`, password: `wrong`)
2. **Expected**: Error message "Invalid credentials" appears
3. **Result**: ⬜ Pass / ⬜ Fail

### 1.3 Valid Login
1. **Action**: Enter valid admin credentials
2. **Expected**: Redirects to dashboard/overview page
3. **Result**: ⬜ Pass / ⬜ Fail

### 1.4 Logout
1. **Action**: Click logout button/link
2. **Expected**: Redirects to login page, session cleared
3. **Result**: ⬜ Pass / ⬜ Fail

### 1.5 Protected Pages Without Login
1. **Action**: Navigate to `http://127.0.0.1:8000/dashboard/` while logged out
2. **Expected**: Redirects to login page
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 📊 Test 2: Dashboard Overview

### 2.1 Overview Page Load
1. **Action**: Navigate to `http://127.0.0.1:8000/dashboard/`
2. **Expected**: Dashboard loads with statistics cards (total logs, anomalies, alerts)
3. **Result**: ⬜ Pass / ⬜ Fail

### 2.2 Recent Anomalies List
1. **Action**: Scroll to "Recent Anomalies" section
2. **Expected**: List of recent anomalies with timestamps and details
3. **Result**: ⬜ Pass / ⬜ Fail

### 2.3 Statistics Cards
1. **Action**: Verify statistics cards display numbers
2. **Expected**: Cards show:
   - Total Logs Processed
   - Anomalies Detected
   - Critical Alerts
   - Active Sources
3. **Result**: ⬜ Pass / ⬜ Fail

### 2.4 Time Range Filter (if available)
1. **Action**: Change time range filter (e.g., Last 24 hours, Last 7 days)
2. **Expected**: Dashboard updates with filtered data
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 🔍 Test 3: Log Details View

### 3.1 View Log Details
1. **Action**: Click on an anomaly from the dashboard list
2. **Expected**: Details page loads showing:
   - Raw log content
   - Anomaly score
   - Timestamp
   - Source system
3. **Result**: ⬜ Pass / ⬜ Fail

### 3.2 Anomaly Acknowledgment
1. **Action**: Click "Acknowledge" button on an anomaly
2. **Expected**: Anomaly marked as acknowledged, button changes state
3. **Result**: ⬜ Pass / ⬜ Fail

### 3.3 View Acknowledged Anomalies
1. **Action**: Navigate to acknowledged anomalies list
2. **Expected**: Previously acknowledged anomalies appear in separate list
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 📡 Test 4: API Endpoints

### 4.1 API Health Check
1. **Action**: GET `http://127.0.0.1:8000/api/health/`
2. **Expected**: JSON response `{"status": "healthy"}`
3. **Result**: ⬜ Pass / ⬜ Fail

**Testing Method:**
```bash
curl http://127.0.0.1:8000/api/health/
```

### 4.2 Submit Log Entry (Authenticated)

**Step 1: Get API Key**
1. Navigate to admin panel: `http://127.0.0.1:8000/admin/`
2. Go to "API Keys" section
3. Create new API key or copy existing key

**Step 2: Submit Log**
```bash
curl -X POST http://127.0.0.1:8000/api/logs/ \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "timestamp": "2025-11-05T10:30:00Z",
    "raw_log": "ERROR: Connection timeout to database server",
    "source": "production-server-01",
    "log_level": "ERROR"
  }'
```

3. **Expected**: JSON response with created log entry
4. **Result**: ⬜ Pass / ⬜ Fail

### 4.3 Submit Log Without API Key
```bash
curl -X POST http://127.0.0.1:8000/api/logs/ \
  -H "Content-Type: application/json" \
  -d '{"timestamp": "2025-11-05T10:30:00Z", "raw_log": "Test log"}'
```

3. **Expected**: 401 or 403 Unauthorized response
4. **Result**: ⬜ Pass / ⬜ Fail

### 4.4 Get Recent Anomalies
```bash
curl http://127.0.0.1:8000/api/anomalies/ \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE"
```

3. **Expected**: JSON array of recent anomalies
4. **Result**: ⬜ Pass / ⬜ Fail

### 4.5 Get Alerts
```bash
curl http://127.0.0.1:8000/api/alerts/ \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE"
```

3. **Expected**: JSON array of alerts
4. **Result**: ⬜ Pass / ⬜ Fail

---

## 📈 Test 5: Analytics Dashboard

### 5.1 Analytics Page Load
1. **Action**: Navigate to `http://127.0.0.1:8000/analytics/dashboard/`
2. **Expected**: Analytics dashboard loads with charts/graphs
3. **Result**: ⬜ Pass / ⬜ Fail

### 5.2 Time Series Chart
1. **Action**: Verify time series chart displays
2. **Expected**: Chart shows anomaly trends over time
3. **Result**: ⬜ Pass / ⬜ Fail

### 5.3 Source Distribution
1. **Action**: Check source distribution chart/table
2. **Expected**: Shows anomalies grouped by source system
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 🖥️ Test 6: System Monitoring

### 6.1 System Metrics Page
1. **Action**: Navigate to `http://127.0.0.1:8000/monitoring/system/`
2. **Expected**: System metrics page loads (CPU, memory, disk usage)
3. **Result**: ⬜ Pass / ⬜ Fail

### 6.2 Real-time Updates (if implemented)
1. **Action**: Keep page open for 30 seconds
2. **Expected**: Metrics auto-refresh or update
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 🔧 Test 7: Admin Panel

### 7.1 Admin Login
1. **Action**: Navigate to `http://127.0.0.1:8000/admin/`
2. **Expected**: Django admin login page appears
3. **Result**: ⬜ Pass / ⬜ Fail

### 7.2 Admin Dashboard Access
1. **Action**: Login with superuser credentials
2. **Expected**: Django admin dashboard loads with all models
3. **Result**: ⬜ Pass / ⬜ Fail

### 7.3 View Log Entries
1. **Action**: Click on "Log entries" in admin panel
2. **Expected**: List of all log entries with filters
3. **Result**: ⬜ Pass / ⬜ Fail

### 7.4 Create API Key
1. **Action**: Navigate to API Keys section → Add API Key
2. **Expected**: New API key created and displayed
3. **Result**: ⬜ Pass / ⬜ Fail

### 7.5 View Anomalies
1. **Action**: Click on "Anomalies" in admin panel
2. **Expected**: List of detected anomalies with details
3. **Result**: ⬜ Pass / ⬜ Fail

### 7.6 Filter by Date Range
1. **Action**: Use date filters in admin panel
2. **Expected**: Results filtered correctly
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 🧪 Test 8: Edge Cases

### 8.1 Empty Database State
1. **Action**: Fresh database with no data
2. **Expected**: Dashboard shows "No data" or 0 values gracefully
3. **Result**: ⬜ Pass / ⬜ Fail

### 8.2 Large Log Submission
1. **Action**: Submit log with 10,000+ character content
2. **Expected**: Log accepted or appropriate error message
3. **Result**: ⬜ Pass / ⬜ Fail

### 8.3 Invalid Timestamp Format
```bash
curl -X POST http://127.0.0.1:8000/api/logs/ \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"timestamp": "invalid-date", "raw_log": "Test"}'
```

3. **Expected**: 400 Bad Request with validation error
4. **Result**: ⬜ Pass / ⬜ Fail

### 8.4 Missing Required Fields
```bash
curl -X POST http://127.0.0.1:8000/api/logs/ \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"raw_log": "Test log"}'
```

3. **Expected**: 400 Bad Request with field error
4. **Result**: ⬜ Pass / ⬜ Fail

### 8.5 SQL Injection Attempt
1. **Action**: Try SQL injection in search/filter fields
   - Example: `'; DROP TABLE logs; --`
2. **Expected**: Input sanitized, no database modification
3. **Result**: ⬜ Pass / ⬜ Fail

### 8.6 XSS Attack Attempt
1. **Action**: Submit log with JavaScript code
   - Example: `<script>alert('XSS')</script>`
2. **Expected**: Code escaped and not executed
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 🌐 Test 9: Browser Compatibility

### 9.1 Chrome/Chromium
1. **Action**: Test all features in Chrome
2. **Expected**: All features work correctly
3. **Result**: ⬜ Pass / ⬜ Fail

### 9.2 Firefox
1. **Action**: Test all features in Firefox
2. **Expected**: All features work correctly
3. **Result**: ⬜ Pass / ⬜ Fail

### 9.3 Mobile Responsive (Chrome Mobile/Firefox Mobile)
1. **Action**: Test on mobile device or browser DevTools mobile view
2. **Expected**: Layout adjusts for mobile screens
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 🔒 Test 10: Security Features

### 10.1 CSRF Protection
1. **Action**: Submit form without CSRF token
2. **Expected**: Request rejected with CSRF error
3. **Result**: ⬜ Pass / ⬜ Fail

### 10.2 Session Timeout
1. **Action**: Login and wait 30+ minutes without activity
2. **Expected**: Session expires, requires re-login
3. **Result**: ⬜ Pass / ⬜ Fail

### 10.3 Password Security
1. **Action**: Try to create user with weak password (e.g., "12345")
2. **Expected**: Password rejected with validation error
3. **Result**: ⬜ Pass / ⬜ Fail

---

## 📝 Test Results Summary

**Date Tested**: _______________  
**Tester Name**: _______________  
**Environment**: Development / Staging / Production

| Test Category | Total Tests | Passed | Failed | Notes |
|--------------|-------------|--------|--------|-------|
| Authentication | 5 | ___ | ___ | |
| Dashboard | 4 | ___ | ___ | |
| Log Details | 3 | ___ | ___ | |
| API Endpoints | 5 | ___ | ___ | |
| Analytics | 3 | ___ | ___ | |
| System Monitoring | 2 | ___ | ___ | |
| Admin Panel | 6 | ___ | ___ | |
| Edge Cases | 6 | ___ | ___ | |
| Browser Compatibility | 3 | ___ | ___ | |
| Security | 3 | ___ | ___ | |
| **TOTAL** | **40** | **___** | **___** | |

---

## 🐛 Bug Report Template

**Bug ID**: _______________  
**Severity**: Critical / High / Medium / Low  
**Test Case**: _______________  
**Description**: _______________  
**Steps to Reproduce**:
1. 
2. 
3. 

**Expected Result**: _______________  
**Actual Result**: _______________  
**Screenshot/Logs**: _______________  

---

## ✅ Sign-off

Manual testing completed by:

**Name**: _______________  
**Date**: _______________  
**Signature**: _______________  

**Overall Result**: ⬜ All Tests Passed / ⬜ Issues Found (see bug reports)

---

## 📞 Support

For issues or questions:
- Check logs: `/home/shun/Desktop/logbert/webplatform/logs/`
- Review documentation: README.md
- Check Django errors: Terminal output where `runserver` is running
