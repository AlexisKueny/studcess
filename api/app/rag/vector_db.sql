create extension if not exists vector;

create table if not exists chunks(
  id uuid primary key default gen_random_uuid(),
  content text not null,
  content_hash text unique,
  embedding vector not null,
  created_at timestamptz not null default now()
);

create or replace function match_chunks(
  query_embedding vector,
  match_count int default 5
)
returns table (id uuid, content text)
language sql stable
as $$
  select c.id, c.content
  from chunks c
  -- <=> is the cosine distance
  order by c.embedding <=> query_embedding
  limit match_count;
$$;