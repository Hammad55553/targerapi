<?php
$host = "ep-sparkling-bar-a5daghxj-pooler.us-east-2.aws.neon.tech";
$dbname = "signup";
$user = "neondb_owner";
$pass = "CeDyTMfmad79";

try {
    $conn = new PDO("pgsql:host=$host;dbname=$dbname", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}
?>
