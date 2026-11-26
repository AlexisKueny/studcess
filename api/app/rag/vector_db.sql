create extension if not exists vector;

create table if not exists chunks(
  id uuid primary key default gen_random_uuid(),
  content text not null,
  embedding vector not null,
  created_at timestamptz not null default now()
);