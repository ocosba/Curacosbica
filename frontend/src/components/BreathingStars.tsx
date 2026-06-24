import { useEffect, useRef } from 'react';

interface Star {
  nx: number;
  ny: number;
  r: number;
  depth: number;
  color: string;
  baseAlpha: number;
  tw: number;
  phase: number;
  big: boolean;
}

interface ShootingStar {
  active: boolean;
  x: number;
  y: number;
  len: number;
  vx: number;
  vy: number;
  life: number;
  nextTriggerTime: number;
}

export function BreathingStars() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationFrameId: number;
    let stars: Star[] = [];
    let lastTime = performance.now();
    let totalTime = 0;

    const shootingStar: ShootingStar = {
      active: false,
      x: 0,
      y: 0,
      len: 0,
      vx: 0,
      vy: 0,
      life: 0,
      nextTriggerTime: 3 + Math.random() * 5 // Initial delay (seconds)
    };

    const dpr = Math.min(window.devicePixelRatio || 1, 2);

    const resize = () => {
      canvas.width = window.innerWidth * dpr;
      canvas.height = window.innerHeight * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      initStars();
    };

    // Color palette based on exactly specified weights
    const getWeightedColor = () => {
      const w = Math.random();
      if (w < 0.60) return '255, 255, 255'; // White
      if (w < 0.78) return '227, 190, 69';  // Gold (#E3BE45)
      if (w < 0.90) return '207, 198, 243'; // Glow (#cfc6f3)
      return '176, 108, 176';               // Orchid (#B06CB0)
    };

    const initStars = () => {
      stars = [];
      
      // Calculate exact number of stars based on width and mobile scaling
      let numStars = 210;
      if (window.innerWidth < 700) {
        numStars = Math.floor(210 * 0.6); // ~126 stars
      }

      for (let i = 0; i < numStars; i++) {
        stars.push({
          nx: Math.random(),
          ny: Math.random(),
          r: Math.random() * 1.5 + 0.4, // radius 0.4 to 1.9px
          depth: Math.random() * 0.06 + 0.01, // parallax factor
          color: getWeightedColor(),
          baseAlpha: Math.random() * 0.5 + 0.4,
          tw: Math.random() * 1.6 + 0.4,
          phase: Math.random() * Math.PI * 2,
          big: Math.random() < 0.12 // 12% probability of big stars with glow
        });
      }
    };

    const triggerShootingStar = (w: number, h: number) => {
      shootingStar.active = true;
      shootingStar.x = Math.random() * w * 0.7;
      shootingStar.y = Math.random() * h * 0.4;
      shootingStar.len = 140 + Math.random() * 120;
      shootingStar.vx = 320 + Math.random() * 180;
      shootingStar.vy = 120 + Math.random() * 90;
      shootingStar.life = 0;
    };

    const draw = (now: number) => {
      const dt = Math.min((now - lastTime) / 1000, 0.05); // cap at 0.05s
      lastTime = now;
      totalTime += dt;

      const W = window.innerWidth;
      const H = window.innerHeight;

      ctx.clearRect(0, 0, W, H);

      // Draw background stars
      stars.forEach(star => {
        // Calculate coordinates with wrapping and parallax
        const x = star.nx * W;
        let y = (star.ny * H - window.scrollY * star.depth) % (H + 40);
        if (y < -20) y += H + 40;

        // Cintilação
        const alpha = star.baseAlpha * (0.55 + 0.45 * Math.sin(totalTime * star.tw + star.phase));

        ctx.beginPath();
        ctx.fillStyle = `rgba(${star.color}, ${alpha})`;

        if (star.big) {
          ctx.save();
          ctx.shadowBlur = 8;
          ctx.shadowColor = `rgba(${star.color}, 0.9)`;
          ctx.arc(x, y, star.r, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        } else {
          ctx.arc(x, y, star.r, 0, Math.PI * 2);
          ctx.fill();
        }
      });

      // Update and draw shooting star
      if (shootingStar.active) {
        shootingStar.x += shootingStar.vx * dt;
        shootingStar.y += shootingStar.vy * dt;
        shootingStar.life += dt;

        const fade = Math.max(0, 1 - shootingStar.life / 1.1);

        if (fade <= 0 || shootingStar.x > W || shootingStar.y > H) {
          shootingStar.active = false;
          // Schedule next shooting star
          shootingStar.nextTriggerTime = totalTime + (6 + Math.random() * 8);
        } else {
          const speed = Math.sqrt(shootingStar.vx * shootingStar.vx + shootingStar.vy * shootingStar.vy);
          const dx = (shootingStar.vx / speed) * shootingStar.len;
          const dy = (shootingStar.vy / speed) * shootingStar.len;

          const grad = ctx.createLinearGradient(
            shootingStar.x,
            shootingStar.y,
            shootingStar.x - dx,
            shootingStar.y - dy
          );
          grad.addColorStop(0, `rgba(255, 255, 255, ${0.85 * fade})`);
          grad.addColorStop(1, 'rgba(255, 255, 255, 0)');

          ctx.beginPath();
          ctx.strokeStyle = grad;
          ctx.lineWidth = 1.6;
          ctx.moveTo(shootingStar.x, shootingStar.y);
          ctx.lineTo(shootingStar.x - dx, shootingStar.y - dy);
          ctx.stroke();
        }
      } else {
        // If not active, check if it's time to trigger a new one
        if (totalTime >= shootingStar.nextTriggerTime) {
          triggerShootingStar(W, H);
        }
      }

      animationFrameId = requestAnimationFrame(draw);
    };

    window.addEventListener('resize', resize);
    resize();
    animationFrameId = requestAnimationFrame(draw);

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'fixed',
        inset: 0,
        width: '100%',
        height: '100%',
        zIndex: 0,
        pointerEvents: 'none',
      }}
    />
  );
}
