

CREATE TABLE IF NOT EXISTS projects (
    project_id INT NOT NULL,
    task_id INT NOT NULL,
    name VARCHAR(64),
    creation_date  TIMESTAMP,
    end_date TIMESTAMP,
    hours INT,
    budget int,
    status VARCHAR(20),
    description VARCHAR(140)
    );

create table if not exists tickets (
	ticket_id int unique not null,
	project_id INT NOT null,
	resource_id INT not null,
    task_id INT NOT null,
	name VARCHAR(64),
	status VARCHAR(32),
	type VARCHAR(20),
	description VARCHAR(140),
	priority int ,
	creation_date timestamp,
	limit_date timestamp,
	primary key(ticket_id, project_id, resource_id, task_id)
    )
-- 	CONSTRAINT fk_task_id FOREIGN KEY(task_id) REFERENCES tasks(task_id),
-- 	CONSTRAINT fk_project_id FOREIGN KEY(project_id) REFERENCES projects(project_id)

create table if not exists tasks (
	task_id INT NOT null,
	resource_id INT not null,
	status VARCHAR(20),
	priority int ,
	description VARCHAR(140),
	estimated_effort int,
	real_effort int,
	primary key(task_id, resource_id)

)

create table if not exists resolutions (
	ticket_id INT not null,
    task_id INT NOT null,
    task_name VARCHAR(64)
    )


create table if not exists resources(
	resource_id int not null primary key,
	name varchar(32),
	surname varchar(32)

)

