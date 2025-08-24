<?php
include '../db.php';

$data = json_decode(file_get_contents("php://input"), true);

if ($data) {
    $query = "INSERT INTO user_data (id, ip_address, latitude, longitude, user_agent, referrer, first_name, last_name, education, university, country, province, city, phone_number, email) 
              VALUES (uuid_generate_v4(), :ip, :lat, :lon, :agent, :referrer, :fname, :lname, :edu, :uni, :country, :province, :city, :phone, :email)";
    
    $stmt = $conn->prepare($query);
    $stmt->execute([
        ':ip' => $data['ip_address'],
        ':lat' => $data['latitude'],
        ':lon' => $data['longitude'],
        ':agent' => $data['user_agent'],
        ':referrer' => $data['referrer'],
        ':fname' => $data['first_name'],
        ':lname' => $data['last_name'],
        ':edu' => $data['education'],
        ':uni' => $data['university'],
        ':country' => $data['country'],
        ':province' => $data['province'],
        ':city' => $data['city'],
        ':phone' => $data['phone_number'],
        ':email' => $data['email'],
    ]);

    echo json_encode(["message" => "Data inserted successfully"]);
} else {
    echo json_encode(["error" => "Invalid data"]);
}
?>
