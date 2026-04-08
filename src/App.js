import React, { useState } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";

function Server({ position, load, power }) {
  const color = power === "Coal" ? "red" : power === "Solar" ? "green" : "blue";
  return (
    <mesh position={position}>
      <boxGeometry args={[1, load / 50, 1]} />
      <meshStandardMaterial color={color} />
    </mesh>
  );
}

export default function App() {
  const [servers, setServers] = useState([
    { cpu: 80, power: "Coal" },
    { cpu: 40, power: "Solar" },
    { cpu: 60, power: "Wind" }
  ]);

  const [wind, setWind] = useState(50);

  const randomize = () => {
    const powers = ["Coal", "Solar", "Wind"];
    setServers(servers.map(() => ({
      cpu: Math.floor(Math.random() * 80) + 20,
      power: powers[Math.floor(Math.random() * 3)]
    })));
    setWind([0, 50, 100][Math.floor(Math.random() * 3)]);
  };

  const moveLoad = () => {
    let newServers = [...servers];
    let coal = newServers.find(s => s.power === "Coal");
    let solar = newServers.find(s => s.power === "Solar");
    if (coal && solar) {
      let moved = Math.floor(coal.cpu * 0.3);
      coal.cpu -= moved;
      solar.cpu += moved;
    }
    setServers([...newServers]);
  };

  const carbonScore = servers.reduce((acc, s) => {
    let factor = s.power === "Coal" ? 3 : s.power === "Solar" ? 1 : 0;
    return acc + s.cpu * factor;
  }, 0);

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <div style={{ width: "75%" }}>
        <Canvas camera={{ position: [5, 5, 5] }}>
          <ambientLight />
          <pointLight position={[10, 10, 10]} />
          <OrbitControls />
          {servers.map((s, i) => (
            <Server key={i} position={[i * 2 - 2, 0, 0]} load={s.cpu} power={s.power} />
          ))}
        </Canvas>
      </div>

      <div style={{ width: "25%", padding: "20px", background: "#eee" }}>
        <h2>Green Ops Control</h2>
        <p>Wind: {wind}%</p>
        <p>Carbon Score: {carbonScore}</p>

        <button onClick={randomize}>Randomize</button><br/><br/>
        <button onClick={moveLoad}>Move Load</button>
      </div>
    </div>
  );
}
