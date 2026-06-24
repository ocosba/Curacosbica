import React from 'react';

// Shared Cosba branding mark component, matching cosbaMark(size, withRays) exactly from 01.html
export function CosbaMark({ size, withRays }: { size: number; withRays: boolean }) {
  const gold = 'var(--c-gold)';
  const lav = 'var(--c-violet)';
  const orchid = 'var(--c-orchid)';

  const rays = [];
  if (withRays) {
    for (let i = 0; i < 40; i++) {
      const a = (i / 40) * Math.PI * 2;
      rays.push(
        <line
          key={'ray' + i}
          x1={Math.cos(a) * 78}
          y1={10 + Math.sin(a) * 78}
          x2={Math.cos(a) * 96}
          y2={10 + Math.sin(a) * 96}
          stroke={lav}
          strokeWidth="1"
          opacity={0.32}
        />
      );
    }
  }

  const dots: React.ReactNode[] = [];
  [0, 45, 135, 180, 225, 315].forEach((deg, i) => {
    const a = (deg * Math.PI) / 180;
    dots.push(
      <circle key={'dot' + i} cx={Math.cos(a) * 66} cy={10 + Math.sin(a) * 66} r="4.2" fill={orchid} />
    );
  });

  const circles = [];
  for (let i = 0; i < 6; i++) {
    const a = (i * Math.PI) / 3;
    circles.push(
      <circle key={'s' + i} cx={Math.cos(a) * 27} cy={10 + Math.sin(a) * 27} r="27" fill="none" stroke={lav} strokeWidth="2" />
    );
  }

  return (
    <svg
      width={size}
      height={size * (228 / 200)}
      viewBox="-100 -128 200 228"
      fill="none"
      style={{ display: 'inline-block' }}
    >
      {rays}
      <circle key="ring" cx="0" cy="10" r="66" fill="none" stroke={orchid} strokeWidth="2.4" />
      {dots}
      <circle key="sc" cx="0" cy="10" r="27" fill="none" stroke={lav} strokeWidth="2" />
      {circles}
      <polygon key="tu" points="0,-96 -21,-60 21,-60" fill="none" stroke={gold} strokeWidth="2.6" />
      <polygon key="td" points="0,-48 -21,-84 21,-84" fill="none" stroke={gold} strokeWidth="2.6" />
      <circle key="eye" cx="0" cy="-72" r="6.5" fill="none" stroke={gold} strokeWidth="2" />
      <circle key="pupil" cx="0" cy="-72" r="2.2" fill={gold} />
    </svg>
  );
}

// Brand mark wrapper components
export function MarkSmall() {
  return <CosbaMark size={42} withRays={false} />;
}

export function MarkGlow() {
  return <CosbaMark size={64} withRays={true} />;
}

// High-fidelity dynamic mandala renderer for the hero section
interface MandalaHeroProps {
  simbolo?: string;
}

export function MandalaHero({ simbolo = 'Flor da Vida' }: MandalaHeroProps) {
  const gold = 'var(--c-gold)';
  const lav = 'var(--c-violet)';
  const orchid = 'var(--c-orchid)';
  const glow = 'var(--c-glow)';

  // Helper to wrap rotating svg groups
  const SpinG = ({ id, dur, rev, children }: { id: string; dur: number; rev: boolean; children: React.ReactNode }) => (
    <g
      key={id}
      style={{
        transformBox: 'fill-box',
        transformOrigin: 'center',
        animation: `arc${rev ? 'SpinR' : 'Spin'} ${dur}s linear infinite`
      }}
    >
      {children}
    </g>
  );

  // Shared outer rotating ticks ring + inner core
  const ticks = [];
  for (let i = 0; i < 48; i++) {
    const a = (i / 48) * Math.PI * 2;
    const r1 = 122;
    const r2 = i % 4 === 0 ? 134 : 128;
    ticks.push(
      <line
        key={'t' + i}
        x1={Math.cos(a) * r1}
        y1={Math.sin(a) * r1}
        x2={Math.cos(a) * r2}
        y2={Math.sin(a) * r2}
        stroke={gold}
        strokeWidth={i % 4 === 0 ? 1.4 : 0.8}
        opacity={i % 4 === 0 ? 0.8 : 0.4}
      />
    );
  }

  const tickRing = (
    <SpinG id="ring1" dur={110} rev={false} key="ring1_g">
      <circle key="rc" cx="0" cy="0" r="122" fill="none" stroke={gold} strokeWidth="1" opacity={0.5} />
      {ticks}
    </SpinG>
  );

  const core = (
    <g key="core">
      <circle key="cg" cx="0" cy="0" r="10" fill="none" stroke={gold} strokeWidth="1.6" />
      <circle key="cp" cx="0" cy="0" r="3.4" fill={gold} />
    </g>
  );

  let layers: React.ReactNode[] = [];

  if (simbolo === 'Cubo de Metatron') {
    const pts = [[0, 0]];
    for (let i = 0; i < 6; i++) {
      const a = (i * Math.PI) / 3;
      pts.push([Math.cos(a) * 44, Math.sin(a) * 44]);
    }
    for (let i = 0; i < 6; i++) {
      const a = (i * Math.PI) / 3;
      pts.push([Math.cos(a) * 88, Math.sin(a) * 88]);
    }
    const lines = [];
    for (let i = 1; i < pts.length; i++) {
      for (let j = i + 1; j < pts.length; j++) {
        lines.push(
          <line
            key={'ml' + i + '_' + j}
            x1={pts[i][0]}
            y1={pts[i][1]}
            x2={pts[j][0]}
            y2={pts[j][1]}
            stroke={lav}
            strokeWidth="0.5"
            opacity={0.3}
          />
        );
      }
    }
    const circ = pts.map((p, i) => (
      <circle
        key={'mc' + i}
        cx={p[0]}
        cy={p[1]}
        r="14"
        fill="none"
        stroke={i === 0 ? gold : lav}
        strokeWidth="1.2"
        opacity={i === 0 ? 0.95 : 0.7}
      />
    ));
    layers = [
      <SpinG id="metatron" dur={160} rev={true} key="metatron_g">
        {lines}
        {circ}
      </SpinG>,
      core
    ];
  } else if (simbolo === 'Merkabah') {
    const triUp = (
      <SpinG id="tria" dur={64} rev={false} key="triUp_g">
        <polygon key="u" points="0,-104 90,52 -90,52" fill="none" stroke={gold} strokeWidth="1.6" opacity={0.82} />
        <circle key="cc" cx="0" cy="0" r="62" fill="none" stroke={gold} strokeWidth="0.6" opacity={0.3} />
      </SpinG>
    );
    const triDown = (
      <SpinG id="trib" dur={64} rev={true} key="triDown_g">
        <polygon key="d" points="0,104 90,-52 -90,-52" fill="none" stroke={orchid} strokeWidth="1.6" opacity={0.82} />
      </SpinG>
    );
    const dots = [];
    for (let i = 0; i < 12; i++) {
      const a = (i / 12) * Math.PI * 2;
      dots.push(
        <circle key={'d' + i} cx={Math.cos(a) * 80} cy={Math.sin(a) * 80} r="2.2" fill={glow} opacity={0.6} />
      );
    }
    layers = [
      <SpinG id="mdots" dur={84} rev={false} key="mdots_g">
        {dots}
      </SpinG>,
      triUp,
      triDown,
      <circle key="eye" cx="0" cy="0" r="14" fill="none" stroke={gold} strokeWidth="1.4" />,
      core
    ];
  } else if (simbolo === 'Toroide') {
    const ell = [];
    for (let i = 0; i < 9; i++) {
      const ang = (i / 9) * 180;
      ell.push(
        <ellipse
          key={'e' + i}
          cx="0"
          cy="0"
          rx="106"
          ry="40"
          fill="none"
          stroke={i % 2 ? orchid : lav}
          strokeWidth="0.9"
          opacity={0.5}
          transform={`rotate(${ang})`}
        />
      );
    }
    const innerEll = [];
    for (let i = 0; i < 7; i++) {
      const ang = (i / 7) * 180;
      innerEll.push(
        <ellipse
          key={'i' + i}
          cx="0"
          cy="0"
          rx="58"
          ry="22"
          fill="none"
          stroke={gold}
          strokeWidth="0.8"
          opacity={0.45}
          transform={`rotate(${ang})`}
        />
      );
    }
    layers = [
      <SpinG id="tor1" dur={100} rev={false} key="tor1_g">
        {ell}
      </SpinG>,
      <SpinG id="tor2" dur={58} rev={true} key="tor2_g">
        {innerEll}
      </SpinG>,
      <circle key="tc" cx="0" cy="0" r="92" fill="none" stroke={gold} strokeWidth="0.6" opacity={0.3} />,
      core
    ];
  } else {
    // Default: Flor da Vida
    const r = 26;
    const fpts = [[0, 0]];
    for (let i = 0; i < 6; i++) {
      const a = (i * Math.PI) / 3;
      fpts.push([Math.cos(a) * r, Math.sin(a) * r]);
    }
    for (let i = 0; i < 6; i++) {
      const a = (i * Math.PI) / 3 + Math.PI / 6;
      fpts.push([Math.cos(a) * r * Math.sqrt(3), Math.sin(a) * r * Math.sqrt(3)]);
    }
    for (let i = 0; i < 6; i++) {
      const a = (i * Math.PI) / 3;
      fpts.push([Math.cos(a) * r * 2, Math.sin(a) * r * 2]);
    }
    const flower = fpts.map((p, i) => (
      <circle
        key={'f' + i}
        cx={p[0]}
        cy={p[1]}
        r={r}
        fill="none"
        stroke={lav}
        strokeWidth="1.2"
        opacity={i === 0 ? 0.9 : 0.6}
      />
    ));
    const merk = (
      <SpinG id="merk" dur={120} rev={true} key="merk_g">
        <polygon key="mu" points="0,-96 83,48 -83,48" fill="none" stroke={orchid} strokeWidth="1.2" opacity={0.5} />
        <polygon key="md" points="0,96 83,-48 -83,-48" fill="none" stroke={orchid} strokeWidth="1.2" opacity="0.5" />
      </SpinG>
    );
    const dots = [];
    for (let i = 0; i < 12; i++) {
      const a = (i / 12) * Math.PI * 2;
      dots.push(
        <circle key={'d' + i} cx={Math.cos(a) * 74} cy={Math.sin(a) * 74} r="2.4" fill={glow} opacity={0.7} />
      );
    }
    layers = [
      merk,
      <SpinG id="dots" dur={60} rev={false} key="dots_g">
        {dots}
      </SpinG>,
      <g key="flower">{flower}</g>,
      core
    ];
  }

  return (
    <svg
      width="min(78vw,360px)"
      height="min(78vw,360px)"
      viewBox="-150 -150 300 300"
      fill="none"
      style={{
        display: 'block',
        filter: 'drop-shadow(0 0 24px color-mix(in oklab, var(--c-orchid) 40%, transparent))',
        animation: 'arcFloat 6s ease-in-out infinite'
      }}
    >
      {tickRing}
      {layers}
    </svg>
  );
}
