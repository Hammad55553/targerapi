<?php
include '../db.php';

$query = "SELECT * FROM user_data";
$stmt = $conn->query($query);
$data = $stmt->fetchAll(PDO::FETCH_ASSOC);

echo json_encode($data);
?>
