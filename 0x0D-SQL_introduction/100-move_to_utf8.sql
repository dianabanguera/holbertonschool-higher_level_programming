-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

--      Database hbtn_0c_0 in utf8
ALTER database hbtn_0c_0 CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
--      Table first_table
ALTER Table hbtn_0c_0.first_table CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
--      Field name in first_table
ALTER Table hbtn_0c_0.first_table MODIFY 'name' VARCHAR(256) CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;

